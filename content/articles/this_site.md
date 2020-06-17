Title: Writing and deploying (this) Blog
Date: 2020-05-9
Modified: 2020-05-16
Tags: Python, Google Cloud Platform, GCP, Pelican, CI/CD
Summary: How this Blog is written, hosted and deployed

## Overview

1. Write articles and pages in [Markdown](https://www.markdownguide.org/getting-started/) file format.
2. Convert Markdown files into static HTML files using [Pelican](https://blog.getpelican.com/), a Python library.
3. Publish the generated static website online.

Furthermore, this whole process can be streamlined to make it really easy to write and publish articles, for this, my choice of tools relies on the Google Cloud Platform (GCP) where I build and host the site using the following services: [Cloud Repositories](https://cloud.google.com/source-repositories) to manage the site source files, [Container Registry](https://cloud.google.com/container-registry) to store a [Docker](https://www.docker.com/) image containing Pelican, [Cloud Build](https://cloud.google.com/cloud-build) to watch for updates on the Blog’s repository, call the Pelican image and generate new content that it’s synced to [Cloud Storage](https://cloud.google.com/storage) where this blog is hosted.
