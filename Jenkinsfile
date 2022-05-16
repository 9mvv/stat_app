#!groovy
// Check ub1 properties
properties([disableConcurrentBuilds()])

pipeline {
    agent {
            label 'local_arm_docker'
        }
    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
        timestamps()
    }
    stages {
        stage("Build image") {
            steps {
                sh 'docker rmi 9vadim/my_images:${IMAGE_TAG} . || true'
                sh 'docker build -t 9vadim/my_images:${IMAGE_TAG} .'
                sh 'docker login -u 9vadim -p ${GIT_HUB_TOKEN}'
                sh 'docker push 9vadim/my_images:${IMAGE_TAG}'
                sh 'docker logout'
            }
        }
    }
}