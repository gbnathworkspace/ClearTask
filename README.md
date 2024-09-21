# ClearTask
Task Management Application with Django (back-end), React (front-end), and AWS (deployment)

Step-by-Step Explanation:
Import Necessary Modules: Import render and JsonResponse from django.shortcuts and django.http respectively.
Define the View Function: Create a function named hello_world that takes an HTTP request as an argument.
Return a JSON Response: Use JsonResponse to return a JSON object with a message.

1.  Import Necessary Modules
render: Typically used to render HTML templates, but not used in this specific view.
JsonResponse: Used to return a JSON response.

2. Define the View Function
hello_world: The name of the view function.
request: The HTTP request object that Django passes to the view.

3. Return a JSON Response
JsonResponse: A Django class that returns a JSON-encoded response.
{'message': 'Hello, World!'}: The dictionary to be converted to JSON.

How This is Achieved in the Context of Your Project
1. Define the View: The hello_world view is defined in tasks/views.py.
2. Add URL Routing: Ensure the view is accessible via a URL by adding it to taskhub/urls.py.

1. Define the View
Your tasks/views.py file:

2. Add URL Routing
Your taskhub/urls.py file should include a URL pattern for the hello_world view:

Step-by-Step Instructions:
Ensure Django Server is Running: Make sure your Django server is running and the API endpoint is accessible.
Fetch Data in React: Use the fetch API or axios to call the Django API endpoint from your React application.
Display Data in React: Update your React component to display the fetched data.
1. Ensure Django Server is Running
Make sure your Django server is running. Open a terminal, navigate to the root directory of your Django project, and run:

Verify that the API endpoint is accessible by navigating to http://127.0.0.1:8000/api/hello/ in your browser. You should see a JSON response:

2. Fetch Data in React
In your React application, use the fetch API or axios to call the Django API endpoint. Update your src/App.js file as follows:

3. Display Data in React
The above code fetches data from the Django API endpoint and updates the state with the fetched message. The message is then displayed in the React component.

Summary
Ensure Django Server is Running: Make sure the Django server is running and the API endpoint is accessible.
Fetch Data in React: Use the fetch API or axios to call the Django API endpoint from your React application.
Display Data in React: Update your React component to display the fetched data.

Final Steps
1. Run Django Server: Ensure the Django server is running.
2. Run React Development Server: Start the React development server.
3. Verify Integration: Open your browser and navigate to http://localhost:3000/. You should see the message "Hello, World!" fetched from the Django backend and displayed in your React app.