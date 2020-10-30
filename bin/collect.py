#!/usr/bin/env python
# -*- coding: utf-8-*-

"""
Webscrape Intercom Help Articles and export them into markdown and html as a JSON data file

This captures Collection info but not Sections.  Images are downloaded into an images folder.
The images are renamed with the collection directory name (see the dir_map dict below) in numerical order.
You will need to dedupe duplicate images using another tool. Renaming the images avoids bad initial names
and duplicate image filenames (quick hack and not ideal - feel free to improve as desired.)

"""

import httpx
from markdownify import markdownify as md
from bs4 import BeautifulSoup
import time
import json
import re

main_url = "https://help.biodati.com"

rootdir = "/Users/william/studio/dev/studio_help"

# Collection Title to directory name
dir_map = {
    "BioDati Studio Overview": "overview",
    "Knowledge": "knowledge",
    "Networks": "networks",
    "Projects": "projects",
    "Developer and API Information": "dev",
    "Administration": "admin",
}

pages = {}


def collect_content():
    """Scrape content from Intercom Articles"""

    page = httpx.get(main_url)

    soup = BeautifulSoup(page.content, "html.parser")

    links = soup.find_all("a", class_="paper")
    collection_links = [f"{main_url}{link['href']}" for link in links]

    for clink in collection_links:
        image_number = 0
        time.sleep(0.5)
        page = httpx.get(clink)
        soup = BeautifulSoup(page.content, "html.parser")
        collection_title = soup("h1")[0].string

        print(f"\n\nProcessing Collection: {collection_title}")

        collection_dir = dir_map[collection_title]
        links = soup("a", class_="paper")
        page_links = [f"{main_url}{link['href']}" for link in links]

        for plink in page_links:
            time.sleep(0.5)
            article_page = httpx.get(plink)
            article_soup = BeautifulSoup(article_page.content, "html.parser")
            article_title = article_soup("h1")[0].string
            print(f"    Article: {article_title}")
            article = article_soup("article")

            article_text = article[0].prettify()

            article_md = md(article_text, heading_style="ATX")

            key = f"{collection_title}__{article_title}"
            if key in pages:
                print(
                    f"Collection {collection_dir} has duplicate Article Title: {article_title}"
                )

            pages[key] = {
                "collection_title": collection_title,
                "article_title": article_title,
                "content_html": article_text,
                "content_md": article_md,
                "image_urls": [],
            }

            for image in article_soup.select("article img"):
                image_url = image.get("src")
                img_fn = image_url.split("/")[-1]
                suffix = img_fn.split(".")[-1]
                if len(suffix) > 4:
                    suffix = "png"

                print("       Suffix", suffix, "FN", img_fn)

                image_save_fn = f"{collection_dir}_{image_number}.{suffix}"
                image_number += 1
                pages[key]["image_urls"].append(
                    {"url": image_url, "filename": image_save_fn}
                )

                result = httpx.get(image_url)

                with open(f"images/{image_save_fn}", "wb") as f:
                    f.write(result.content)

    with open("pages.json", "w") as f:
        json.dump(pages, f, indent=4)


def process_content():

    with open("pages.json", "r") as f:
        pages = json.load(f)

    fnav = open("nav.yml", "w")

    last_collection = ""
    for key in pages:
        page = pages[key]
        collection_key = dir_map[page["collection_title"]]

        # Clean up content
        content = page["content_md"]

        content = re.sub("^\s+", "", content, flags=re.MULTILINE)
        content = re.sub("\s*$", "", content, flags=re.MULTILINE)
        content = re.sub("^\s+$", "", content, flags=re.MULTILINE)

        for img in page["image_urls"]:
            content = content.replace(
                f"![]({img['url']})", f"\n![[{img['filename']}]]\n"
            )

        content = re.sub(r"^(\!\[\[.*?\]\])\s*$", r"\1\n", content, flags=re.MULTILINE)

        # Create article_fn
        article_fn = page["article_title"]
        article_fn = article_fn.lower()
        article_fn = article_fn.replace(" ", "_").replace("/", "_").replace(":", "")
        article_fn = f"{article_fn}.md"

        if collection_key != last_collection:
            fnav.write(f"  - {page['collection_title']}:\n")
            last_collection = collection_key
        fnav.write(
            f"    - {page['article_title']}: sections/{collection_key}/{article_fn}\n"
        )

        doc_fn = f"../docs/sections/{collection_key}/{article_fn}"
        print("Doc fn", doc_fn)
        with open(doc_fn, "w") as f:
            f.write(f'# {page["article_title"].strip()}\n\n')
            f.write(content)
            f.write("\n")


def main():

    # collect_content()

    process_content()


if __name__ == "__main__":
    main()
