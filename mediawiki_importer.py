#!/usr/bin/env python

import mariadb
import settings
import subprocess
import sys


def run_grabber(grabber):
    subprocess.run([
        'php', f'grabbers/{grabber}.php',
        '--url', settings.api_url,
        '--username', settings.wiki_username,
        '--password', settings.wiki_password
    ])


try:
    conn = mariadb.connect(
        user=settings.db_user,
        password=settings.db_pass,
        host=settings.db_host,
        database=settings.db_name
    )
except mariadb.Error as e:
    print(f'Error connecting to db: {e}')
    sys.exit(1)

cursor = conn.cursor()

with open('clean_db.sql') as f:
    cursor.execute(f.read().decode('utf-8'), multi=True)

conn.close()

run_grabber('grabText')
run_grabber('grabDeletedText')
run_grabber('grabLogs')
run_grabber('grabFiles')
run_grabber('grabDeletedFiles')
run_grabber('grabUserBlocks')
run_grabber('grabUserGroups')
run_grabber('grabProtectedTitles')
run_grabber('grabAbuseFilter')

subprocess.run([ 'php', 'grabbers/populateUserTable.php' ])