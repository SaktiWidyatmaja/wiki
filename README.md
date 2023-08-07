# Wikipedia-like Online Encyclopedia

This project is a web application that simulates a Wikipedia-like online encyclopedia. Users can view encyclopedia entries, search for entries, create new entries, edit existing entries, and even access random entries. Entries are written in Markdown and are converted to HTML for display.

## Getting Started

To get started with the project, follow these steps:

1. Download the distribution code from [this link](https://cdn.cs50.net/web/2020/spring/projects/1/wiki.zip) and unzip it.
2. Open the `encyclopedia/urls.py` file to see the URL configuration for the app.
3. Examine `encyclopedia/util.py` which contains utility functions for working with encyclopedia entries.
4. Check the `entries/` directory to see pre-created sample entries.
5. Take a look at `encyclopedia/views.py` which defines the views for the app.

## Features

This Wikipedia-like Online Encyclopedia project offers the following features:

1. **Entry Page:** Visit `/wiki/TITLE` to render an encyclopedia entry's content.
   - The content is retrieved using the provided utility function.
   - If the entry does not exist, an error page is shown.

2. **Index Page:** The `index.html` template lists all entries as links.
   - Clicking on an entry name takes you directly to that entry's page.

3. **Search:** Search for an entry by typing a query in the sidebar.
   - Matching query redirects to the entry's page.
   - Non-matching query displays search results with substring matches.

4. **Create New Page:** Click "Create New Page" to create a new entry.
   - Enter a title and Markdown content in a textarea.
   - Save the page, or receive an error if the title already exists.

5. **Edit Page:** On an entry's page, click "Edit" to modify its Markdown content.
   - Existing content is pre-populated in the textarea.
   - Save the changes and be redirected back to the entry.

6. **Random Page:** Click "Random Page" to view a random entry.

7. **Markdown to HTML Conversion:** Markdown content is converted to HTML using the `python-markdown2` package.
   - Headings, bold text, unordered lists, links, and paragraphs are supported.

## Usage

1. Install the required packages using `pip3 install -r requirements.txt`.
2. Run the Django server with `python manage.py runserver`.
3. Access the app in your browser at `http://localhost:8000`.

## Acknowledgments

This project is based on the CS50 Web Programming course by Harvard University.

---