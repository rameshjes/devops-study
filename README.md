# learn-devops


## What is DevOps?

![DevOps](https://github.com/rameshjes/learn-devops/blob/main/images/what_is_devops.png)

**Integration**: For integration, **Jenkins** or any other automation server e.g Github actions, Gitlab can also be used.

**Build**: Place where all of the code is compiled.

**Testing**: For testing, one can use tools e.g pytest(for Python), Junit (for Java). This includes unit testing.

**Deploy**: To deploy the project on server, we can use **Docker**

**Monitor**: There are also montioring tools, that can monitor the status of the project

---
**What is Jenkins**: An open source automation server which **enables developers** to reliably **build, test, and deploy their software.**

---
## DevOps Stages

1. **Version Control**: It maintains different versions of the code. Keeps track of code commits, which devlopers has committed what, we can go to previous version anytime too.s
		Example : Git, SVN
2. **Continuous Integration**: This includes: Compile, validate, Code Review, Unit Testing(testing each part of code), Integration Testing (how different parts of project work together), making a package 
		Note that: These all tasks falls under build category too.
	
3. **Continuous Delivery**: Also Continous Testing. This step basically considers: Deploying the build application to test servers. 

4. **Continuous Deployment**: Deploying the tested application on the production server for release.


![DevOps_Stages](https://github.com/rameshjes/learn-devops/blob/main/images/devops_stages.png)


## CI and CD Pipeline

Normally pipeline consists of the following blocks as shown in below image.

**Version Control**: Help us to track of code. One can fall back anytime on previous code.

**Build**: Stage whole code in the project is build. All the formatting of the code is done in this part.

**Testing**: Unit testing of the function is performed

**Deploy, Auto Test, and Deploy to production**: In this stage, your code is deployed to the testing/stage server, where you can test your project. Once you have tested the project thoroughly, then it is deployment on to the production phase. 

**Note that: If we find bug in the testing server, one can fix and push the code, similarly whole pipeline is run again**


![CI_CD_Pipeline](https://github.com/rameshjes/learn-devops/blob/main/images/ci_and_cd_pipeline.png)


### What is Continuous Integration (CI)?


Continuous Integration (CI) is a **development practice where developers integrate code into a shared repository frequently, preferably several times a day.** Each integration can then be verified by an automated build and automated tests.

**This process is called continuous, because all the steps e.g build, testing are done continously**

Also Several developers can push the changes simultaneously.

![what_is_CI](https://github.com/rameshjes/learn-devops/blob/main/images/what_is_ci.png)

### What is Continuous Delivery (CD)?

After CI, Continuous Delivery is the next step.

Continuous Delivery is the **ability to get changes of all types—including new features, configuration changes, bug fixes and experiments—into production, or into the hands of users, safely and quickly in a sustainable way.**

**This process is called continuous, because all the steps e.g build, testing, deployment are done continously**


![what_is_CD](https://github.com/rameshjes/learn-devops/blob/main/images/what_is_cd.png)

---
### What is Jenkins

* Jenkins is an **open source automation tool** written in Java with plugins built for **Continuous Integration purpose.** 
* Its plugins allows integration of various DevOps stages.

#### Importance of Jenkins

Once user commits the code, Jenkins takes over from that.
**Note that** : Jenkins is only **Continuous Integration** tool, so once this process is completed, then we need to deploy to the server.

![what_is_CD](https://github.com/rameshjes/learn-devops/blob/main/images/jenkins.png)

---

### How project is Deployed to the server?

* To do this, **Docker** is used. 
* Once the product is moved to the Staging server, we need the tools like **Docker** to deploy it. 
* Now **what is Docker** : It is virtualization environment, which we can create on the fly.
![Docker](https://github.com/rameshjes/learn-devops/blob/main/images/docker.png)

* To deploy the product, we need to replicate the environment, where we can run our project. Thats what **Docker** provide to us.
![Docker_Importance](https://github.com/rameshjes/learn-devops/blob/main/images/docker_importance.png)
