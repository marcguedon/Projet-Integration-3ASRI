# PROJET INTEGRATION - 3A SRI

## Installation du workspace

Le dossier est considéré comme le ROS workspace, il n'est donc pas utile de créer un dossier `catkin_ws`.\
Ainsi, à la racine, cloner le répo.
```console
cd ~
git clone https://github.com/marcguedon/Projet-Integration-3ASRI.git
```

Il faut maintenant cloner le package `motoman` qui est une dépendance à notre package MoveIt.
```console
cd Projet-Integration-3ASRI/src
git clone https://github.com/ros-industrial/motoman.git
```

Maintenant que les dépendances sont installées, il faut build le package `hc10_moveit_config`.
```console
cd ..
. /opt/ros/noetic/setup.bash
catkin build
```

Il est a présent possible de sourcer le fichier `devel/setup.bash` qui a été généré.
```console
. devel/setup.bash
```

Pour s'assurer que le package est correctement build, vous pouvez lancer le launch file de démonstration:
```console
roslaunch hc10_moveit_config demo.launch
```

### Utilisation de ROS (et du package) dans un terminal

A chaque fois qu'un nouveau terminal est ouvert et que vous voulez utiliser une commande ROS (avec notamment notre package), il faut sourcer les fichiers `.bash` à la racine du projet.
```console
cd /home/etudiant/Projet-Integration-3ASRI
. /opt/ros/noetic/setup.bash
. devel/setup.bash
```

## Génération du package MoveIt

Pour générer le package MoveIt du robot HC10, lancer le setup assistant de MoveIt. Une nouvelle fenêtre doit s'ouvrir.
```console
roslaunch moveit_setup_assistant setup_assistant.launch
```

Cliquer sur "Create New MoveIt Configuration Package", et spécifier le chemin vers le fichier `hc10.xacro` qui se trouve dans le package motoman précédemment cloné (`/home/etudiant/Projet-Integration-3ASRI/src/motoman/motoman_hc10_support/urdf/hc10.xacro`).\
Lors de la première génération du package nous avons également ajouter l'argument `hand:=true`, mais il n'est peut être pas utile de l'ajouter, car le guide précise: "To enable the optionally available hand in your robot model, add the following xacro argument to the corresponding text field: hand:=true".\
Vous pouvez alors cliquer sur "Load files".

Nous allons passer sur chacun des onglets qui se trouve sur la gauche de la fenêtre. Si un onglet n'est pas présent dans ce fichier, c'est parce qu'il n'a pas été touché. De même pour les valeurs.

### Self Collisions

- Cliquer sur le bouton "Generate Collision Matrix" (c'est tout).

### Virtual Joints

- Cliquer sur le bouton "Add Virtual Joint"
- Saisir "virtual_joint" pour "Virtual Joint Name"
- Choisir "base_link" dans "Child Link"
- Saisir "world" dans "Parent Frame Name"
- Choisir "fixed" dans Joint Type
- Cliquer sur le bouton "Save"

### Planning Groups

- Cliquer sur le bouton "Add Groups"
- Saisir "hc10_arm" dans "Kinematics" - "Group Name"
- Choisir "kdl_kinematics_plugin/KDLKinematicsPlugin" dans "Kinematic Solver"
- Cliquer sur le bouton "Add Joints"
- Sélectionner tous les joints présents dans "Available Joints" et cliquer sur le bouton ">" pour les mettre dans "Selected Joints"
- Cliquer sur le bouton "Save"

### Robot Pose

- Cliquer sur le bouton "Add Pose"
- Saisir "Home" dans "Pose Name"
- Mettre la position de chaque joint à 0
- Cliquer sur le bouton "Save"

### End Effectors

- Cliquer sur le bouton "Add End Effector"
- Saisir "cam_support" dans "End Effector Name"
- Choisir "tool0" dans "Parent Link"
- Cliquer sur le bouton "Save"

### Simulation (je ne sais pas si il est important de garder ce fichier URDF ou non)

- Cliquer sur "Generate URDF"
- Copier/coller le contenu dans un ficiher `.urdf`

### Author Information (obligatoire pour créer le package)

- Saisir votre nom/prénom dans "Name of the maintainer"
- Saisir votre adresse mail dans "Email of the maintainer"

### Configuration Files

- Cliquer sur le bouton "Browse"
- Créer un dossier `hc10_moveit_config` dans le dossier `/home/etudiant/Projet-Integration-3ASRI/src`
- Cliquer sur le bouton "Generate Package"

Une fois le package généré, vous pouvez quitter le Setup Assitant.

## Autre

Je ne sais pas si le fichier hc10_robot.urdf sera utile ou non, il est donc dans la racine du projet. N'hésitez pas à le déplacer si nécessaire.