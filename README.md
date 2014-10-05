Intercom Folder
===============
Quick hack to automatically download segment data from Intercom into a Dropbox folder.

Setup
-----
1. Create a file main.cfg
2. Create a Dropbox app from dropbox.com/developers App Console.
3. Generate an implicit token for yourself
4. Get your app_id and app_key from Intercom
5. Get the id for the segments your wish to track (easiest way is to go to the segment and look at the url)
6. Input it into the config template below

[Dropbox]
access_token: <Dropbox Implicit Access Token>

[Intercom]
app_id: <Your Intercom App Id>
app_key: <Your Intercom App Key>

[IntercomSegments]
<Name of the Segment Folder>: <Segment Id>

7. Run `python main.py` on a cron (or whenever you feel like)

Footnote
--------
Let me know if you find this useful or have questions. I'm just posting it publicly just for the hell of it, obviously semi-perfectly documenting it. I'm @ehfeng.