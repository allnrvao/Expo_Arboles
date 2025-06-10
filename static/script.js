function construirArbolNodo(nombre, arbol) {
  const nodo = { text: { name: nombre } };
  const hijos = arbol[nombre] || [];

  if (hijos.length > 0) {
    nodo.children = hijos.map(hijo => construirArbolNodo(hijo, arbol));
  }

  return nodo;
}

async function cargarArbolJerarquico() {
  const res = await fetch('/ver_arbol_jerarquico');
  const arbol = await res.json();

  const padres = Object.keys(arbol);
  const todosHijos = new Set(Object.values(arbol).flat());
  const posiblesRaices = padres.filter(p => !todosHijos.has(p));

  if (posiblesRaices.length === 0) {
    document.getElementById('tree-container').innerHTML = '<p class="text-muted">No hay datos suficientes.</p>';
    return;
  }

  const raiz = posiblesRaices[0];

  const estructura = {
    chart: {
      container: "#tree-container",
      levelSeparation: 100,
      siblingSeparation: 100,
      subTeeSeparation: 80,
      nodeAlign: "TOP",
      connectors: {
        type: "step",
        style: { "stroke-width": 2, "stroke": "#1976d2" }
      },
      node: { HTMLclass: "nodeExample1" },
      animateOnInit: false,
      padding: 20
    },
    nodeStructure: construirArbolNodo(raiz, arbol)
  };

  document.getElementById('tree-container').innerHTML = '';
  new Treant(estructura);
}

document.getElementById('formPersona')?.addEventListener('submit', async (e) => {
  e.preventDefault();
  const persona = document.getElementById('persona').value.trim();
  if (!persona) return;

  const res = await fetch('/agregar_pessoa', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ persona })
  });

  if (res.ok) {
    document.getElementById('persona').value = '';
    document.getElementById('persona-container').style.display = 'none';
    cargarArbolJerarquico();
  }
});

document.getElementById('formRelacion')?.addEventListener('submit', async (e) => {
  e.preventDefault();
  const persona1 = document.getElementById('persona1').value.trim();
  const persona2 = document.getElementById('persona2').value.trim();
  if (!persona1 || !persona2) return;

  const res = await fetch('/agregar_relacionamento', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ persona1, persona2 })
  });

  if (res.ok) {
    document.getElementById('persona1').value = '';
    document.getElementById('persona2').value = '';
    cargarArbolJerarquico();
  }
});

window.addEventListener('DOMContentLoaded', cargarArbolJerarquico);
