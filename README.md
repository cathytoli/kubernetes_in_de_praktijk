# workshop 'Kubernetes in de praktijk'
#### Opzet van een simpel kubernetes cluster op een lokale machine. 
Wat heb je nodig om een API te laten draaien waarbij we requests willen doen om data uit een database te halen.

### Vooraf te installeren

- kubectl: brew install kubectl
- docker: brew install docker--cask
- minikube: brew install minikube

### Stappen om het cluster op te zetten en de services deployen
1. Ga via je terminal naar de deployment folder
2. run: minikube start 
3. run: bash deploy.sh
4. run: minikube tunnel

Bovenstaande stappen zorgen ervoor:
- Dat minikube lokaal een cluster opzet. 
- Vervolgens wordt het bash script uitgevoerd waarin alle stappen doorlopen worden om al het benodigde in het cluster aan te maken. 
- Ten slotte wordt de API service opengesteld voor het internet door er een IP adres aan toe te kennen.

##### Deployment templates
Om aan kubernetes kenbaar te maken wat er allemaal aangemaakt moet worden zijn er deployment templates aangemaakt. Dit zijn yaml files.
- API: deployment + service
- database: deployment + service
- persistentVolume + persistentVolumeClaim
- secrets
