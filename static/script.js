document.addEventListener('DOMContentLoaded', () => {
    mostrarArbol();
});

function insertar() {
    const valor = document.getElementById('valor').value;
    if (!valor) return alert("Por favor ingresa un valor.");

    fetch('/insertar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ valor: valor })
    })
    .then(() => {
        mostrarArbol();
        document.getElementById('valor').value = '';
    });
}

function ordenar() {
    fetch('/ordenar', { method: 'POST' })
        .then(() => mostrarArbol());
}

function mostrarArbol() {
    fetch('/mostrar_arbol')
        .then(res => res.json())
        .then(data => {
            const contenedor = document.getElementById('arbol');
            contenedor.innerHTML = '';
            const treeHTML = crearNodo(data);
            contenedor.appendChild(treeHTML);
        });
}

function crearNodo(nodo) {
    if (!nodo) return;

    const nodoDiv = document.createElement('div');
    nodoDiv.classList.add('nodo-arbol');

    const valorDiv = document.createElement('div');
    valorDiv.classList.add('valor-nodo');
    valorDiv.textContent = nodo.valor;

    nodoDiv.appendChild(valorDiv);

    if (nodo.izquierda || nodo.derecha) {
        const hijosDiv = document.createElement('div');
        hijosDiv.classList.add('hijos');

        hijosDiv.appendChild(crearNodo(nodo.izquierda) || document.createElement('div'));
        hijosDiv.appendChild(crearNodo(nodo.derecha) || document.createElement('div'));

        nodoDiv.appendChild(hijosDiv);
    }

    return nodoDiv;
}
