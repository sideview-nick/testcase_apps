# testcase_apps

As of this writing this is a pair of small testcase apps,  designed to test python imports and to reproduce various problems where 
an app A will at runtime end up importing code that ships inside app B instead of the code that it itself ships. 

Install both apps in your Splunk deployment, and go to the "Test App A" landing page to proceed. 

WARNING:   the modular inputs as written currently will index data into index=main. 
