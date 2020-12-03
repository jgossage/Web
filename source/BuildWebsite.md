# Build a Website
This blog will try to suggest a way of developing a website for personal use. It
is probably of most interest to people who have some background in computing
since it makes heavy use a number of computer based tools during the development
and maintenance of the site.

This is not a recipe, rather it is a guide. It could only be considered a recipe
by those who have a computing environment that is close to identical to that
wich I have. Anyone else will need to adapt some of the details described in
this blog to their environment.

The blog has three parts:
# General Principles
## Website Purpose
   The clarity of your purpose for creating a website will have a strong effect
   on the nature of your website. People have many different reasons for
   developing websites and there are many technologies available to help with
   the process.
## Website Environment
The following sections describe why the environment of your website is critical
to  the success of the website.
#### Ease of Maintenance of the Website
#### Cost of Operating the Website
### Local Website
#### Nature
##### Network Connectivity
###### Name and Address
###### Bandwidth
##### Flexibility
#### Advantages
##### Total Control
#### Downsides
##### Bandwith Management
##### Address Stability
##### Maintenance
### Hosted Website
#### Nature
#### Advantages
#### Downsides
### Preparing Content
#### Nature
#### Local Computer
#### Editing via the Web
# My Website
My website is hosted on [*GitHub*](https://github.com/) and uses
[`GitHub Pages`](https://pages.github.com/) with [Jekyll](https://jekyllrb.com)
to build and manage the website
remotely from my local computer. This means that I use
[Git](https://git-scm.com/) to maintain the source text for my blogs.

I run [Windows 10 Home Edition](https://www.microsoft.com/windows) as the
operating system on my local computer and use
[Microsoft Visual Studio Code](https://code.visualstudio.com/) as my text editor
for generating website content locally and for general maintenance of my computer system.
## Purpose
## Nature
### GitHub
#### GitHub Usage
#### Accounts
#### Repositories
#### GitHub Pages
#### Jekyll
### Local Computer
#### Network Connectivity
#### Content Generation
#### Content Maintenance
#### Website Maintenance
# Building My Website
## Overview
## Construction
### Prepare the Local Site
### Create Remote Repsitory
    First create a repository on `GitHub` to hold the source material for your website. The repository can have any name that you wish. The repository should have a prototype `README.MD` file and may contain a `LICENSE` file if `GitHub` supports the licence that you want to use for your repository materials.
### Create `gh-pages` *Git* branch in your *GitHub* repository.
### Clone Remote Repository on Local Computer
    This places a copy of your remote repository on your local computer.
### Create `gh-pages` `*Git* Branch` in Local Repository
    Make this the default *Git* branch.
### Create a file called `index.md` as Home Page for the Base Document
    This file will be the base document for your website and can contain
    anything that you like.
### Check your Work Into *Git*
    This has now prepared your site to be sent to *GitHub*.
### Push your work to *GitHub*
    This makes your *GitHub* repository capable of containing the source
    material for your website.
### Make Your `GitHub` Repository be a `GitHub Pages` Source Repository
    You need to access the `settings` for the repository. Scroll down the
    `settings` page until you find a section dealing with `GitHub Pages`.\
    Then perform the following steps:
    * Turn on the `gh-pages` option.\
      You do this by specifying `gh-pages` as the selected `source` for your
