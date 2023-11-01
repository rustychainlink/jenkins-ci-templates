# Basic Jenkins
A bare-bones implementation of Jenkins utilzing [configuration-as-code](https://plugins.jenkins.io/configuration-as-code/). \
Along with [Prometheus](https://prometheus.io/) and [Grafana](https://grafana.com/) for scraping and visualizing metrics.
<html>
<img src="https://www.jenkins.io/images/logos/JCasC/JCasC.svg" alt="Basic Jenkins" width="200" height="200">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Prometheus_software_logo.svg/2066px-Prometheus_software_logo.svg.png" alt="Prometheus Logo" width="200" height="200">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Grafana_icon.svg/351px-Grafana_icon.svg.png" alt="Grafana Logo" width="200" height="200">
</html>

Requires `Docker` and `docker-compose`.
Basic usage:
```bash
. setup.sh
jenkins-local
# Please specify a valid option:
#     --casc     (view local jenkins casc docs)
#     --in       (ssh into running container)
#     --check    (validate pipeline code)
#     --jobdsl   (view local jenkins job dsl)
#     --logs     (view running container logs)
#     --down     (undeploy container)
#     --purge    (purge all container traces)
#     --rebuild  (rebuild container)
#     --up       (deploy container)
```

## References
- [Monitoring Jenkins with Grafana and Prometheus](https://youtu.be/3H9eNIf9KZs?si=SIso_zwlA90x04yp)
