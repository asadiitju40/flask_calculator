pipeline {
    agent any

    triggers {
        // Everyday 10:30AM
       // cron('30 10 * * *')
        
        // Every 5 mins
        cron('H/5 * * * *')
    }
    
    environment {
        IMAGE_NAME = "flask-calculator"
        CONTAINER_NAME = "flask-calculator"
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Stop Previous Container') {
            steps {
                sh """
                docker stop ${CONTAINER_NAME} || true
                docker rm ${CONTAINER_NAME} || true
                """
            }
        }

        stage('Run Docker Container') {
            steps {
                sh "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}"
            }
        }
    }

    post {
        success {
            echo "✅ App deployed successfully at http://<your-server-ip>:5000"
        }
        failure {
            echo "❌ Build or deploy failed."
        }
    }
}
