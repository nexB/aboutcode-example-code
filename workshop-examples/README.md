# Procedure
Each group should choose one example here to begin with. 

### Codebase Prep
The example codebase directories contain archive files, so start by extracting them:
  * Using your standard OS's un-archive tool
  * Or using `extractcode --shallow` from ScanCode Toolkit
Ex:
```
$ extractcode --shallow example-1/
Extracting archives...
[####################] 2
Extracting done.
```

### Run ScanCode scan
Now that the codebase is extracted and prepped, we can run a comprehensive scan

Ex:
```
// Long version
$ scancode --copyright --license --info --package --email --url example-1/ --json-pp ~/example-1-scan-results.json

// short version
$ scancode -clipeu example-1/ --json-pp ~/example-1-scan-results.json
```

### View Scan Results using AboutCode Manager
Now, to view the results we need to start the AboutCode Manager program.

Once running, load the scan by:
  * clicking `File ==> Import Json File`
  * Navigate to your scanfile (`example-1-scan-results.json`)
  * Follow the promp and save the resulting SQLite DB file to location of your choice

If all goes well, you will be dropped into the Dashboard View, and greeted with a few graphs.

From here, use the Chart Summary view and Table View to examine and interpret the results

### Make Conclusions and Export
Once you have made some interpretations and are ready to record your conclusions:
  * Open the Node View and navigate to the location where you wish to record the conclusions
  * Click on the Node's name in the Node View to open the Conclusions Prompt.
  * Fill out the relevant details 
  * Hit save

To view and export your conclusions:
  * navigate to Component Summary View
  * Export by clicking the Export button in the format of your choice
