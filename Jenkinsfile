pipeline {
    agent any

    environment {
        COMPOSE_FILE = "docker-compose.yml"
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Stop Existing Stack') {
            steps {
                sh "docker compose down || true"
            }
        }

        stage('Build & Start Services') {
            steps {
                sh "docker compose up -d --build"
            }
        }

        stage('Verify Running') {
            steps {
                sh "docker ps"
            }
        }
    }

    post {
        success {
            echo "✅ Full stack deployed (App + Monitoring)"
        }
        failure {
            echo "❌ Deployment failed"
        }
    }
}
