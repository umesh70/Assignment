# Assignment 

This repository contains a docker image and the code for the assignment qeuestion.


## Prerequisites

Ensure you have the following installed on your system:
- Docker
- Git
- Python3

## Docker image Build

1. **Clone the Repository**:
    ```sh 
    git clone https://github.com/umesh70/assignment.git
2. **Move into the directory and Build the Docker file**:
   ```sh
    cd assignment
3. **Build the docker file**
    ```sh
    docker build -t assignment .
4. **Run the docker image**
    ```sh
    docker run -p 5000:5000 -e FLASK_APP=server.py assignment
 ## Accessing Endpoints

 ### Open Postman 
1. **For Accessing all the users**
    
    - Copy the below URL and select **GET** from method list and hit send
    ```sh
    http://127.0.0.1:5000/users

2.  **For Creating a new User**
- Add the new user details in raw option of body in the following format(key value format)
    ```sh
        {
            "name":"name",
            "password":"password",
            "email":"email"
        }
    
- Copy the below URL and select **POST** from method list and hit send
    ```sh
    http://127.0.0.1:5000/users
3. **For Accessing a particular user**
- Copy the below URL and select **GET** from method list and hit send
    ```sh
    http://127.0.0.1:5000/users/userID

    replace the userID with actual userID
4. **For Deleting a particular user**
- Copy the below URL and select **DELETE** from method list and hit send
    ```sh
    http://127.0.0.1:5000/users/userID

    replace the userID with actual userID

5. **for Updating the existing user**
- Enter the new data of the user in raw option of body in key-value format
-  Copy the below URL and select **PUT** from method list and hit send
    ```sh
    http://127.0.0.1:5000/users/userID

    replace the userID with actual userID
## Application Structure
- The application is divided into different modules for the purpose of scalability.
- The databases, routes are managed in their respective modules, so that when we need to add more enpoints and thier collections it can easily be achieved.
- Blueprints has been used for modularity.