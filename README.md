# ETL for fraud data detection project

**Setup steps:**



1)Skip this step if you have already installed Docker on your machine:
Install Docker based on your machine type from here: https://docs.docker.com/get-docker/

or here:
https://download.docker.com/mac/stable/21090/Docker.dmg

2)Click on the installed Docker app to start the Docker engine.

3)Download the zip file for the project as below
https://github.com/fauzia-s/fraud_data_detection_project

<img width="899" alt="Screen Shot 2021-10-25 at 4 05 44 PM" src="https://user-images.githubusercontent.com/25311137/138792396-f12501d0-20de-4e8e-98a9-8c505a0e90af.png">


4)Unzip the downloaded file.

5)Copy and paste the input datasets to the downloaded dir:
'fraud_data_detection_project-main/data' 

Download the input datasets from here, if you don't have it already.
https://drive.google.com/drive/folders/1mk6_tqVwkK89F6VvQ4XO4ZT5aPIU_rP4

<img width="380" alt="Screen Shot 2021-10-25 at 6 41 58 PM" src="https://user-images.githubusercontent.com/25311137/138792489-03f1b622-e1a9-4e77-b393-7ce781311210.png">

6)Open the terminal window and go to the folder `fraud_data_detection_project-main`:
<img width="687" alt="Screen Shot 2021-10-25 at 8 21 42 PM" src="https://user-images.githubusercontent.com/25311137/138792682-a1e1559c-e8f5-4ae9-b045-0091113e0a65.png">


7)Run the below command inside the dir `fraud_data_detection_project-main` :
`chmod -Rf 777 *`

6)From the same dir, Run the command 
`docker-compose up`

7)Once the services are initialized and you see the below on your terminal (wait for the second "Airflow" sign like this or wait 25-30 secs after running the command, so that all the services are intialized before we try to connect.)

<img width="923" alt="Screen Shot 2021-10-25 at 5 24 52 PM" src="https://user-images.githubusercontent.com/25311137/138792695-1f3151ce-1733-4159-bed3-f2b63d0bb2cd.png">



8)Go to your web browser and type:
`localhost:8080`

9)When you see the login window like below, type user as `admin` and password as `admin1234` and sign in.
This will open up the Airflow UI.

<img width="805" alt="Screen Shot 2021-10-25 at 5 02 38 PM" src="https://user-images.githubusercontent.com/25311137/138792720-586f7903-a16d-40ce-8dc4-5df27bcf2034.png">

10)Go to DAGs tab and click as below.
<img width="1263" alt="Screen Shot 2021-10-25 at 5 06 10 PM" src="https://user-images.githubusercontent.com/25311137/138792729-cd9daf72-fcc4-4633-b60c-e377c4ad5e6a.png">


The Dag should be completed as below:
<img width="1262" alt="Screen Shot 2021-10-25 at 8 39 39 PM" src="https://user-images.githubusercontent.com/25311137/138794066-85d17ffe-127e-4bfd-a365-3265c41f384c.png">

11) You can connect to any client like MySQL Workbench or Aginity Pro to connect to your Postgresql DB to check the tables loaded.

Identity table:
<img width="1267" alt="Screen Shot 2021-10-24 at 4 47 19 PM" src="https://user-images.githubusercontent.com/25311137/138795139-74fc9dbc-38e7-4cf2-8014-67dd3a690139.png">

Transaction table:
<img width="1508" alt="Screen Shot 2021-10-24 at 12 34 53 PM" src="https://user-images.githubusercontent.com/25311137/138795143-9ff8246c-827e-4de5-bbc8-41978c0d7c13.png">

Sample join:
<img width="777" alt="Screen Shot 2021-10-24 at 4 46 58 PM" src="https://user-images.githubusercontent.com/25311137/138795141-ecafb7b1-40a7-4157-b411-c129d89fdf78.png">




**Troubleshooting**:

A)If there are any errors while connecting to the localhost airflow.

B) You see the below error when trying to trigger the DAG:

"The scheduler does not appear to be running.

The DAGs list may not update, and new tasks will not be scheduled."

Solution:
Repeat the steps if it still fails to initialize. This could be because some housekeeping steps we're missed due to abrupt ending of the services. Generally thrid time's a charm!

 `docker-compose down  --volumes --remove-orphans`
 
 `docker-compose up`
