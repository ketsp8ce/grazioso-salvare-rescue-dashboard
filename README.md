## Branch Structure
- **original** – preserved snapshot of the original CS340 artifact
- **enhancement** – current development branch where the environment is rebuilt and improved


# cs340-grazioso-salvare-rescue-dashboard

#Creator: Hunter Marx
#Process for replication

1) Required functionality:
- MongoDB + Dash dashboard to identify rescue dogs for Grazioso Salvare. Filters by breed/age/rescue type. Includes data table + geolocation charts. CS 340 Project Two
*MISSING SCREENSHOTS - Connection functionality unsucessfuly due to faulty host. Final project unable to retrieve data. User plans to recreate outside of apporto in the future and will push updates to this repo.

2) Tools used in environment configuration
- MongoDB (Used as the database to store and query data. MongoDB is ideal due to easy Python integration with Pymongo and flexible NoSQL structure)
- Dash (web framework for building dashboard UI. Provided the view structure as widgets/charts etc. Provided the controller structure as callback functions. This allowed reactive UI updates without Javascript.)
- Apporto (used so to streamline software configuration - replaceable with local environment)
- Jypiter notebook (for client side scripting)
- Python (a portable CRUD module)

3) Steps to complete project:
- import database server side and set up credentials
- Code python module for CRUD functionality
- Test CRUD functionality from ipynb client side
- Code Dash UI with filters
- Test Functionality

4) Challenges
- My greatest challenge was establishing consistent connectivtiy. I ended up coding many try and catch statements and continously making my error handling more robust until I had very specific information on what was going wrong. This lead me to discover that my connectivity with MongoDB was working, but my connectivity with the host was not. I plan to configure my local system so I am continue the development of this project, at which point I will push my updates to this repo.
- Included are screenshots of the empty dashboard as well as the connection error
  ![image](https://github.com/user-attachments/assets/70fe02eb-c872-4ece-8730-25b3c9f9e6dd)
  ![image](https://github.com/user-attachments/assets/e4db5f85-9ceb-4c5d-b0aa-8cae5fd064cc)

Reflection Questions (module 8)
1) How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?
- When writing programs that are maintainable, readable, and adaptable, it is important to focus on the main principals of object oriented design - high cohesion, low coupling, and encapsulation, as well as the principles of modularity - composability, decomposability, continuity, understandability, protection. In laymans terms, it is best to have each component of an application be self contained and portable, with a few as possibly functional dependencies, but with the ability to be called on by other components. In the case of our CRUD Python module, it contained basic connectivity and method outlines. These features were able to be called upon by the front end user interacting with a dashboard. This allowed the front and back end to "talk" to each other. The CRUD module was also vague and self contained enough that it could be reused for future projects with minimal edits.

2) How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?
- This was my first time working on a both the client and server development in a single given project. This gave a high level of abstraction with which to review and interact with the architecture of the application. I was able to keep in mind how this architucture worked at every step, which allowed me to solve problems as they came up. This was also my first time working with a database and writing queries. All past projects in past classes have had me work on one perspective of an application, such as back end with configuring my workspace and build, or front end code that directly interacted with user input. This was the first of I plan to be many projects where I need to keep the big picture architecture in mind.

3) What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?
- Grazioso Salvare had a reocurring problem of working with a database in order to match rescue animals with real world scenerios. As computer scientists our role was to automate this process with as much allowance for efficiency and precision as possible. At the end of the day, the role of software development is simply solving a reocurring problem to allow for streamlined and efficient solutions.
