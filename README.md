# MediaWiki Importer

Script I made to automate a migration process into MediaWiki containers.

See: https://www.mediawiki.org/wiki/Manual:Grabbers

```sh
$ git clone https://gerrit.wikimedia.org/r/mediawiki/tools/grabbers.git 

$ git clone https://github.com/rekyuu/mediawiki_importer
```

Update `settings.py` to your definitions and execute the script from the root of your new MediaWiki installation.

```sh
$ python mediawiki_importer/mediawiki_importer.py
```