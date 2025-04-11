pipeline {
    agent any

    environment {
        VENV = 'venv'
        PYTHON = 'python3'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Kinjalrk2k/simple-ml-model-jenkins-deployment.git'
            }
        }

        stage('Set Up Python Env') {
            steps {
                sh '''
                    $PYTHON -m venv $VENV
                    . $VENV/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                    . $VENV/bin/activate
                    python train.py
                '''
            }
        }

        stage('Test Model') {
            steps {
                sh '''
                    . $VENV/bin/activate
                    python test.py
                '''
            }
        }

        stage('Deploy Model') {
             steps {
                sh '''
                    echo "✅ Model is already saved in model/model.pkl"
                '''
                archiveArtifacts artifacts: 'model/model.pkl', fingerprint: true
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning up workspace...'
            cleanWs()
        }
    }
}
