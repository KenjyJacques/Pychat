function executeCode() {
    const code = editor.getValue(); // Récupérer le code écrit dans CodeMirror
    const outputElement = document.getElementById('console-output');

    fetch('/execute', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ code: code }) // Envoyer le code au serveur
    })
    .then(response => response.json())
    .then(data => {
        // Afficher la sortie dans la console
        outputElement.innerHTML = ''; // Nettoyer la console précédente
        const output = document.createElement('pre');
        output.textContent = data.output;
        outputElement.appendChild(output);
    })
    .catch(error => {
        outputElement.innerHTML = 'Erreur : ' + error;
    });
}
