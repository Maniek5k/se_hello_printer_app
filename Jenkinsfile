pipeline {
    agent any
    stages {
        stage('Deps') {
            steps {
	            sh 'make deps'
        	}
        }
        stage('Lint') {
            steps {
                sh 'make lint'
            }
        }
        stage('Test') {
            steps {
                sh 'make test'
            }
        }
        stage('Additional') {
            steps {
                sh 'make test_complexity'
                sh 'make test_xunit || true'
                xunit thresholds: [
                    skipped(failureThreshold: '0'),
                    failed(failureThreshold: '1')
                    ],
                    tools: [
                        JUnit(deleteOutputFiles: true,
                        failIfNotNew: true,
                        pattern: 'test_results.xml',
                        skipNoTestFiles: false,
                        stopProcessingIfError: true)
                    ]
            }
        }
    }
}