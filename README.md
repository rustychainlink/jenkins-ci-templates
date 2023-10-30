# Basic Jenkins
A bare-bones implementation of Jenkins utilzing [configuration-as-code](https://plugins.jenkins.io/configuration-as-code/).
<html>
<img src="https://www.jenkins.io/images/logos/JCasC/JCasC.svg" alt="Basic Jenkins" width="200" height="200">
</html>

Requires `Docker` and `docker-compose`.
Basic usage:
```bash
. setup.sh
jenkins-local
# Please specify a valid option:
#     --casc 	    (view local jenkins casc docs)
#     --in 	        (ssh into running container)
#     --check 	    (validate pipeline code)
#     --jobdsl 	    (view local jenkins job dsl)
#     --logs 	    (view running container logs)
#     --down 	    (undeploy container)
#     --purge 	    (purge all container traces)
#     --rebuild     (rebuild container)
#     --up 	        (deploy container)
```
