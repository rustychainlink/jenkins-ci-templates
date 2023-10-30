# A minimal Jenkins-as-code implementation (don't use in production)!
FROM jenkins/jenkins:latest
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"

# Install the plugins
COPY ./plugins.txt ${JENKINS_HOME}/.
RUN jenkins-plugin-cli --verbose --plugin-file "$JENKINS_HOME"/plugins.txt

# Inject the jenkins-casc.yaml describing the jenkins config
COPY ./jenkins.yaml ${JENKINS_HOME}/jenkins.yaml

# Notes:
# - https://github.com/jenkinsci/configuration-as-code-plugin/blob/master/README.md
