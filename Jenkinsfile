pipeline {
    agent any

    environment {
        DOCKER_BUILDKIT = "0"
    }

    stages {

        stage('Debug Environment') {
            steps {
                sh '''
                echo "=== Docker Version ==="
                docker --version

                echo "=== Compose Version ==="
                docker-compose --version

                echo "=== Workspace ==="
                pwd
                ls -la
                '''
            }
        }

        stage('Stop Existing Stack & Cleanup') {
            steps {
                sh '''
                echo "Stopping existing containers..."
                docker-compose down --remove-orphans || true

                echo "Removing any leftover containers using port 5000..."
                docker ps -q --filter "publish=5000" | xargs -r docker stop || true
                docker ps -aq --filter "publish=5000" | xargs -r docker rm || true
                '''
            }
        }

        stage('Build & Start Services') {
            steps {
                sh '''
                echo "Building and starting stack..."
                docker-compose up -d --build
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                echo "=== Running Containers ==="
                docker ps

                echo "=== Listening Ports ==="
                netstat -tulpn || true
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful (Flask + Monitoring stack)"
            echo "🌐 App: http://<server-ip>:5000"
        }
        failure {
            echo "❌ Deployment failed"
        }
        always {
            echo "ℹ️ Pipeline finished"
        }
    }
}
