![DMS](https://user-images.githubusercontent.com/37212234/147994631-75beee9d-dbe2-4dbc-85d9-05deba8d763e.png)
Discord Media Searcher is an open-source brute forcer. It has a flexible config and pretty intuitive usage.

DMS currently working on: Python 3.*

# Installation
Install python requests module
<pre><code>$ pip install requests</code></pre>

# Configuring
Go to `config file` and **recommend:** change `database_path` to your database path or **not recommend:** use `keywords` and `formats` variables.
If you using `database_path`, then go to `database file` and paste all file formats which can be used in *link file format* under `__FORMATS`, then paste all file names which can be used in *link filename* under `__KEYWORDS`.
I recommend you use `database file` because I think you gonna use a lot of filenames.

# Using
Start main.py
<pre><code>$ python main.py</code></pre>
Just wait for valid link
It will look like this: `https://cdn.discordapp.com/attachments/01010010100101001/01000010101001001001/HelloWorld.hlw <Response [200]>`

# Good Luck
Thank you for using DMS!
