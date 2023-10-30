#! /bin/bash

# ---------------------------------------------------------------------------- #
# A basic CLI to ease the Jenkins development workflow
# ---------------------------------------------------------------------------- #

declare -A jenkins_cmds=( \
    ["--up"]='_deploy_container' \
    ["--down"]='_undeploy_container' \
    ["--rebuild"]='_rebuild_container' \
    ["--in"]='_ssh_into_running_container' \
    ["--jobdsl"]='_view_local_jenkins_job_dsl' \
    ["--casc"]='_view_local_jenkins_casc_docs' \
    ["--logs"]='_view_running_container_logs' \
    ["--purge"]='_purge_all_container_traces' \
    ["--check"]='_validate_pipeline_code' \
)

function jenkins-local() {
    for cmd in "${!jenkins_cmds[@]}"; do
        if [ "$1" = "$cmd" ]; then
            shift 1
            "${jenkins_cmds[$cmd]}" "$@"
            return 0
        fi
    done
    echo "Please specify a valid option:"
    for cmd in "${!jenkins_cmds[@]}"; do
        printf "    %s \t" "$cmd"
        help_txt="$(echo "${jenkins_cmds[$cmd]}" | sed 's/_/ /g')"
        printf "(%s)" "${help_txt:1}"
        printf "\n"
    done
    return 1
}

_view_local_jenkins_job_dsl() {
    url="http://localhost:8080/plugin/job-dsl/api-viewer/index.html"
    firefox "$url" 
    echo "Opened URL to local instance"
}

_view_local_jenkins_casc_docs() {
    url="http://localhost:8080/manage/configuration-as-code/reference"
    firefox "$url"
    echo "Opened URL to local instance"
}

_view_running_container_logs() {
    docker logs "$(docker ps -aq | head -1)" "$@"
}

_ssh_into_running_container() {
    docker exec -it "$(docker ps -aq)" /bin/bash
}

_rebuild_container() {
    docker-compose build --no-cache
}

_deploy_container() {
    docker-compose up --build -d
}

_undeploy_container() {
    docker-compose down
}

_purge_all_container_traces() {
    _undeploy_container
    docker rm "$(docker ps -aq)"
    docker rmi --force "$(docker images -aq)"
    yes | docker system prune
    yes | docker volume prune
}

_validate_pipeline_code() {
    JENKINS_USERNAME="admin"
    JENKINS_URL="localhost:8080"
    JENKINS_PASSWORD="password"
    echo "Assuming default params:"
    echo "JENKINS_URL: ${JENKINS_URL}"
    echo "JENKINS_USERNAME: ${JENKINS_USERNAME}"
    echo "JENKINS_PASSWORD: ${JENKINS_PASSWORD}"
    if [ -z "$1" ]; then
        echo "Must specify path to Jenkinsfile"
    fi
    jenkinsfile="$1"
	curl --user "$JENKINS_USERNAME:$JENKINS_PASSWORD" -X POST -F "jenkinsfile=<$jenkinsfile" "$JENKINS_URL/pipeline-model-converter/validate"

}
