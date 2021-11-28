# Dockerized-and-Non-Dockerized-App
Model on breast cancer prediction is built on Jupyter notebook. Using the data prediction will be made and the model will detect the type of cancer.

To run the model following commands will be used :
First install all the basic libraries which will be used in notebook. Install pandas, sklearn, seaborn matplotlib.
Then install jupyter notbook and open it with the following command:
jupyter notebook

Open Cancer_prediction file in which the code is present and model is saved.
Model is saved using JobLib library.

Under deploy folder files are their which are required for deploying the model.
Model.pkl file which was saved was moved to the deploy folder.

Under app.py file code is present in which model is wrapped into API and it will be deployed and then dockerized.
For wrapping model to API Flask is installed and used.

app object is created to point the instances to the file name present. Route method is used for exposing the url and on that  URL when the user goes to the /predict method then POST method will be used in which data will be passed in the body of the request and then model will detect the type of cancer.
In postman, URL will be hit for predict method and then data will be sent in the body. In the reponse cancer type will be displayed.

Run the application using following command:
python app.py
Server will be up and running and port number will be displayed. Then access the url localhost:3000.

Open blazemeter and run it and then run one test case by loading the web page. Then once it will run then report will be displayed in which Max users, Avg Throughput and Avg Response time will be displayed.

To dockerize the application, server will be run on docker container. Requirement.txt file will be saved for all the dependencies. Then Docker file will be created and some instructions will be created to pull the image from python. All the code files will be copied into /app folder. 
Run following command:
pip install -r requirements.txt

Open Docker Desktop and build the image using following command:
docker build -t breast_cancer_class:1.0 .

Start container using following command:
docker run -p 5000:3000 breast_cancer_class:1.0

Now access the url via localhost:5000

Open blazemeter and run it and then run one test case by loading the web page. Then once it will run then report will be displayed in which Max users, Avg Throughput and Avg Response time will be displayed.
