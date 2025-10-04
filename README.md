# Vecto - Route Tracking and Fleet Management System

Vecto is a web-based application designed for route tracking, fleet management, and job dispatching. It provides a real-time mapping solution for dispatchers to manage drivers and for drivers to handle job assignments.

## Features

-   **Real-Time Location Tracking:** Monitor driver locations on a live map.
-   **Job Management:** Create, assign, and track jobs from origin to multiple destinations.
-   **Route Optimization:** Automatically calculate the most efficient routes for multi-stop jobs.
-   **Role-Based Views:** Separate user interfaces for dispatchers (admins) and drivers.
-   **Public Tracking Links:** Share temporary, real-time tracking links with customers.
-   **Secure Authentication:** User sign-in powered by Google Authentication.

## Getting Started

To get the application running locally, you will need to set up a Firebase project and a Google Maps API key.

### 1. Prerequisites

-   [Node.js](https://nodejs.org/) (which includes npm)
-   [Firebase CLI](https://firebase.google.com/docs/cli#install-cli-mac-windows-linux)

### 2. Firebase Project Setup

1.  **Create a Firebase Project:**
    -   Go to the [Firebase Console](https://console.firebase.google.com/).
    -   Click "Add project" and follow the on-screen instructions to create a new project.

2.  **Add a Web App to Your Project:**
    -   In your new project's dashboard, click the web icon (`</>`) to add a new web app.
    -   Register the app with a nickname (e.g., "Vecto Web"). **Do not** check the box for Firebase Hosting at this stage.
    -   After registering, Firebase will provide you with a configuration object. You can close this window, as the app is set up to get this configuration automatically.

3.  **Enable Firebase Services:**
    -   In the Firebase Console, go to the **Build** section.
    -   **Authentication:** Click "Get started" and enable the **Google** sign-in provider.
    -   **Firestore Database:** Click "Create database," start in **test mode** (for now), and choose a location for your database.
    -   **Storage:** Click "Get started" and follow the prompts to enable Cloud Storage.

### 3. Google Maps API Key Setup

1.  **Create a Google Cloud Project:**
    -   The application requires a Google Maps API key. This is managed through the [Google Cloud Console](https://console.cloud.google.com/). Your Firebase project is already a Google Cloud project.

2.  **Enable Required APIs:**
    -   In the Google Cloud Console, navigate to the **APIs & Services > Library**.
    -   Search for and enable the following APIs:
        -   **Maps JavaScript API**
        -   **Directions API**
        -   **Places API**
        -   **Routes API**

3.  **Create an API Key:**
    -   Navigate to **APIs & Services > Credentials**.
    -   Click **+ CREATE CREDENTIALS** and select **API key**.
    -   Copy the generated API key.

4.  **Restrict the API Key (Recommended):**
    -   For security, you should restrict your API key. Click on the new key and apply the following restrictions:
        -   Under **Application restrictions**, select **HTTP referrers (web sites)** and add `http://localhost:5000` for local testing.
        -   Under **API restrictions**, select **Restrict key** and choose the four APIs you enabled in the previous step.

### 4. Running the Application Locally

1.  **Clone the Repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Log in to Firebase:**
    ```bash
    firebase login
    ```

3.  **Set Up the Project Alias:**
    -   This project is configured to use a debug project alias. Open the `.firebaserc` file in the root directory.
    -   Replace `"route-tracker-debug"` with your Firebase project ID.
    ```json
    {
      "projects": {
        "default": "YOUR_FIREBASE_PROJECT_ID"
      }
    }
    ```

4.  **Start the Firebase Emulator:**
    -   The emulator provides a local environment for hosting and Firestore.
    -   Run the following command from the root of the project directory:
    ```bash
    firebase emulators:start --only hosting,firestore
    ```

5.  **Access the Application:**
    -   Open your web browser and navigate to `http://localhost:5000`.
    -   The application should load.

6.  **Add the Google Maps API Key:**
    -   Click the settings icon (⚙️) in the top-right corner of the application.
    -   In the "API Keys" section, paste your Google Maps API key into the input field.
    -   Click "Save Key & Reload." The map should now load and become functional.

The application is now running locally and connected to your Firebase project. You can start creating users, companies, and jobs.