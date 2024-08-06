---
title: "Facilitating Programming-based 3D Computer-Aided Design using Bidirectional Programming"
description: ""
date: 2021-11-09
authors:
  - name: "Gonzalez, J. Felipe" 
    me: true
redirect_link : "https://cil.csit.carleton.ca/bidirectional-programming-csg-cad/"

categories:
  - "Technology"
  - "Research"
  - "HCI"
tags:
  - "HCI"
  - "VR"
  - "Haptics"

draft: false
---


## Abstract

3D Computer-Aided Design (CAD) applications allow users to create visual representations of models, helping create, edit, test, and analyze designs. Most offer a Graphical User Interface (GUI) with direct manipulation providing easy-to-use interactions, while a less popular category adopts a programming-based approach requiring users to describe models using specific programming languages. Programming-based CAD applications provide multiple benefits to 3D design, but their use remains limited, potentially due to higher entry barriers and extensive programming requirements. Regrettably, a profound lack of understanding of the challenges faced by users of programming-based CAD applications prevents a clear comprehension of the issues of these applications. Furthermore, research addressing CAD challenges has predominantly focused on applications that provide direct manipulation interactions. This doctoral thesis aims to improve the usability of programming-based CAD applications, focusing on their role in Personal Digital Fabrication with 3D printers. Our research seeks to understand and address programming-based CAD users' challenges during the design process. In our first study, we interviewed twenty OpenSCAD users, a leading programming-based CAD application in the 3D printing community. Data analysis via a Reflexive Thematic Analysis (RTA) led to the development of a comprehensive codebook categorizing three main themes: user profiles, 3D design challenges, and 3D printing challenges. Our second study addressed the identified design challenges in linking 3D views with code and difficulties in performing spatial transformations on the model. We proposed to address these difficulties by introducing the concept of bidirectional programming in programming-based CAD, allowing users to interact with both the code and the view. We modified the source code of OpenSCAD to implement this approach, developing bidirectional navigation features and allowing users to edit the model by interacting with the view while the application updates the code coherently. The third study addressed the keystone challenge of defining geometric properties in parametric designs. After analyzing thirty OpenSCAD models, we developed bidirectional programming features in OpenSCAD to facilitate the definition of parametric properties, directly extracting information from the view to use in the code. Experimentation with OpenSCAD users showed our solution may streamline design, reduc