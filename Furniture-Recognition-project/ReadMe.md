# Furniture-Recognition-Flask
After training the custom classifier using Watson Visual Recognition to identify furniture, 
in particular Tables, Beds and Chairs. (You can follow this to create a custom model on IBM Watson Studio: https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/visual-recognition-create-model.html) . After training the model we are then going to connect my trained custom classifier to a Flask app. Flask is a python web framework used for making web apps. 
I am then going to deploy my Flask app to IBM Cloud. Once the app is deployed on IBM Cloud anyone can 
access the Flask app via a webpage anywhere using a custom link.

Enter the API Key and Classifier Key for Your Service  in config.py

Execute the following commands:

%%bash

ibmcloud config --check-version=false

ibmcloud login --no-region

cloud_emailid

password


%%bash

ibmcloud account orgs


%%bash

ibmcloud target --cf-api https://api.eu-gb.cf.cloud.ibm.com -r eu-gb -o nipunmehar1234@gmail.com

ibmcloud account space-create computer-vision-app


%%bash

ibmcloud target -s computer-vision-app

## Tools
Python |
Open CV |
IBM Cloud |
IBM Visual Recognition |
Watson Studio


### Follow me on GitHub For more and feel free to contact me at nipunmehar10@gmail.com .
