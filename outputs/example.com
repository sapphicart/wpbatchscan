{
  "banner": {
    "description": "WordPress Security Scanner",
    "version": "4.0.1",
    "sponsor": "An Automattic endeavor"
  },
  "db_update_started": true,
  "db_files_updated": [
    "metadata.json",
    "wp_fingerprints.json",
    "timthumbs-v3.txt",
    "config_backups.txt",
    "db_exports.txt",
    "backup_folders.txt",
    "dynamic_finders.yml",
    "LICENSE",
    "sponsor.txt"
  ],
  "db_update_finished": true,
  "scan_aborted": "The remote website is up, but does not seem to be running WordPress.",
  "target_url": "https://example.com/"
}
