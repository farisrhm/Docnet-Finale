
{% extends 'document.html' %}
{% block content %}

<div classe="tableau">
<center>
<table>

<thead>
<tr><td>Nom</td><td>Spécialité</td><td>Disponibilité</td><td>Détails</td></tr>
</thead>

<tbody>
    {% for medecin in medecins %}
<tr><td>{{medecin[1]}}</td> <td>{{medecin[2]}}</td><td>{{medecin[3]}}</td><td><input type=submit name="reserver" value="Réserver" /></td></tr>

    {% endfor %}
    </tbody>
</table>

</center>
</div>
<br>
<br>
{% endblock %}
