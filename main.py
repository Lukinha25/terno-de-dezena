from flask import Flask, render_template_string

app = Flask(__name__)

HTML_APP = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="Fechamento JB">
  <title>Fechamento Terno e Duque</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://w3.org viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🍀</text></svg>">
  <style>
    :root {
      --bg: #0f172a;
      --card: #1e293b;
      --text: #f8fafc;
      --muted: #94a3b8;
      --primary: #10b981;
      --primary-hover: #059669;
      --border: #334155;
      --danger: #ef4444;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    body {
      background-color: var(--bg);
      color: var(--text);
      padding: 20px 16px 40px;
      max-width: 500px;
      margin: 0 auto;
    }

    header {
      text-align: center;
      margin-bottom: 18px;
      padding-top: 8px;
    }

    header h1 {
      font-size: 1.4rem;
      font-weight: 700;
      margin-bottom: 4px;
    }

    header p {
      font-size: 0.85rem;
      color: var(--muted);
    }

    .tabs {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      background: var(--card);
      padding: 6px;
      border-radius: 14px;
      border: 1px solid var(--border);
      margin-bottom: 16px;
    }

    .tab-btn {
      padding: 10px;
      border: none;
      border-radius: 10px;
      background: transparent;
      color: var(--muted);
      font-size: 0.9rem;
      font-weight: 700;
      cursor: pointer;
    }

    .tab-btn.active {
      background: var(--primary);
      color: #064e3b;
    }

    .card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 16px;
      margin-bottom: 16px;
    }

    .form-group {
      margin-bottom: 14px;
    }

    .row-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
    }

    label {
      display: block;
      font-size: 0.85rem;
      font-weight: 600;
      margin-bottom: 6px;
      color: var(--muted);
    }

    select, input {
      width: 100%;
      padding: 12px;
      border-radius: 10px;
      border: 1px solid var(--border);
      background: var(--bg);
      color: var(--text);
      font-size: 1rem;
      outline: none;
    }

    select:focus, input:focus {
      border-color: var(--primary);
    }

    .btn {
      width: 100%;
      padding: 14px;
      border: none;
      border-radius: 12px;
      font-size: 1rem;
      font-weight: 700;
      cursor: pointer;
      margin-top: 6px;
    }

    .btn-primary {
      background: var(--primary);
      color: #064e3b;
    }

    .btn-primary:active {
      background: var(--primary-hover);
    }

    .btn-copy {
      background: #3b82f6;
      color: #ffffff;
      margin-bottom: 12px;
    }

    .error {
      color: var(--danger);
      font-size: 0.85rem;
      margin-top: 8px;
      text-align: center;
      display: none;
    }

    .summary {
      display: flex;
      justify-content: space-between;
      font-size: 0.85rem;
      color: var(--muted);
      margin-bottom: 12px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--border);
    }

    .summary strong {
      color: var(--primary);
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 8px;
      max-height: 360px;
      overflow-y: auto;
      padding-right: 4px;
    }

    .combo-item {
      background: var(--bg);
      border: 1px solid var(--border);
      padding: 10px;
      border-radius: 8px;
      text-align: center;
      font-family: monospace;
      font-size: 1rem;
      font-weight: 600;
      letter-spacing: 1px;
    }

    .hidden {
      display: none;
    }
  </style>
</head>
<body>

  <header>
    <h1>Fechamento de Dezenas</h1>
    <p id="subtituloHeader">Terno: 3 Grupos • 64 Combinações</p>
  </header>

  <div class="tabs">
    <button type="button" class="tab-btn active" id="tabBtnTerno" onclick="mudarAba('terno')">Terno (3 Grupos)</button>
    <button type="button" class="tab-btn" id="tabBtnDuque" onclick="mudarAba('duque')">Duque (2 Grupos)</button>
  </div>

  <div id="abaTerno">
    <div class="card">
      <div class="form-group">
        <label for="t_grupo1">1º Grupo (Bicho)</label>
        <select id="t_grupo1"></select>
      </div>

      <div class="form-group">
        <label for="t_grupo2">2º Grupo (Bicho)</label>
        <select id="t_grupo2"></select>
      </div>

      <div class="form-group">
        <label for="t_grupo3">3º Grupo (Bicho)</label>
        <select id="t_grupo3"></select>
      </div>

      <div class="row-2">
        <div class="form-group">
          <label for="t_valorTotal">Aposta Total (R$)</label>
          <input type="number" id="t_valorTotal" value="10" step="0.50" min="1">
        </div>
        <div class="form-group">
          <label for="t_cotacao">Cotação (x)</label>
          <input type="number" id="t_cotacao" value="15000" step="100" min="1">
        </div>
      </div>

      <button type="button" class="btn btn-primary" onclick="gerarTerno()">Gerar 64 Combinações</button>
      <p id="t_erroMsg" class="error">Por favor, escolha 3 grupos diferentes.</p>
    </div>

    <div id="t_resultadoCard" class="card hidden">
      <div class="summary">
        <span>Por jogo: <strong id="t_valorPorJogo">R$ 0,15</strong></span>
        <span>Retorno: <strong id="t_retornoEstimado">R$ 2.343,75</strong></span>
      </div>

      <button type="button" class="btn btn-copy" id="t_btnCopiar" onclick="copiarJogos('terno')">Copiar Todas as 64 Combinações</button>

      <div id="t_listaCombinacoes" class="grid"></div>
    </div>
  </div>

  <div id="abaDuque" class="hidden">
    <div class="card">
      <div class="form-group">
        <label for="d_grupo1">1º Grupo (Bicho)</label>
        <select id="d_grupo1"></select>
      </div>

      <div class="form-group">
        <label for="d_grupo2">2º Grupo (Bicho)</label>
        <select id="d_grupo2"></select>
      </div>

      <div class="row-2">
        <div class="form-group">
          <label for="d_valorTotal">Aposta Total (R$)</label>
          <input type="number" id="d_valorTotal" value="10" step="0.50" min="1">
        </div>
        <div class="form-group">
          <label for="d_cotacao">Cotação (x)</label>
          <input type="number" id="d_cotacao" value="300" step="10" min="1">
        </div>
      </div>

      <button type="button" class="btn btn-primary" onclick="gerarDuque()">Gerar 16 Combinações</button>
      <p id="d_erroMsg" class="error">Por favor, escolha 2 grupos diferentes.</p>
    </div>

    <div id="d_resultadoCard" class="card hidden">
      <div class="summary">
        <span>Por jogo: <strong id="d_valorPorJogo">R$ 0,35</strong></span>
        <span>Retorno: <strong id="d_retornoEstimado">R$ 107,14</strong></span>
      </div>

      <button type="button" class="btn btn-copy" id="d_btnCopiar" onclick="copiarJogos('duque')">Copiar Todas as 16 Combinações</button>

      <div id="d_listaCombinacoes" class="grid"></div>
    </div>
  </div>

  <script>
    const grupos = [
      { id: 1, nome: "01 - Avestruz", dezenas: ["01", "02", "03", "04"] },
      { id: 2, nome: "02 - Águia", dezenas: ["05", "06", "07", "08"] },
      { id: 3, nome: "03 - Burro", dezenas: ["09", "10", "11", "12"] },
      { id: 4, nome: "04 - Borboleta", dezenas: ["13", "14", "15", "16"] },
      { id: 5, nome: "05 - Cachorro", dezenas: ["17", "18", "19", "20"] },
      { id: 6, nome: "06 - Cabra", dezenas: ["21", "22", "23", "24"] },
      { id: 7, nome: "07 - Carneiro", dezenas: ["25", "26", "27", "28"] },
      { id: 8, nome: "08 - Camelo", dezenas: ["29", "30", "31", "32"] },
      { id: 9, nome: "09 - Cobra", dezenas: ["33", "34", "35", "36"] },
      { id: 10, nome: "10 - Coelho", dezenas: ["37", "38", "39", "40"] },
      { id: 11, nome: "11 - Cavalo", dezenas: ["41", "42", "43", "44"] },
      { id: 12, nome: "12 - Elefante", dezenas: ["45", "46", "47", "48"] },
      { id: 13, nome: "13 - Galo", dezenas: ["49", "50", "51", "52"] },
      { id: 14, nome: "14 - Gato", dezenas: ["53", "54", "55", "56"] },
      { id: 15, nome: "15 - Jacaré", dezenas: ["57", "58", "59", "60"] },
      { id: 16, nome: "16 - Leão", dezenas: ["61", "62", "63", "64"] },
      { id: 17, nome: "17 - Macaco", dezenas: ["65", "66", "67", "68"] },
      { id: 18, nome: "18 - Porco", dezenas: ["69", "70", "71", "72"] },
      { id: 19, nome: "19 - Pavão", dezenas: ["73", "74", "75", "76"] },
      { id: 20, nome: "20 - Peru", dezenas: ["77", "78", "79", "80"] },
      { id: 21, nome: "21 - Touro", dezenas: ["81", "82", "83", "84"] },
      { id: 22, nome: "22 - Tigre", dezenas: ["85", "86", "87", "88"] },
      { id: 23, nome: "23 - Urso", dezenas: ["89", "90", "91", "92"] },
      { id: 24, nome: "24 - Veado", dezenas: ["93", "94", "95", "96"] },
      { id: 25, nome: "25 - Vaca", dezenas: ["97", "98", "99", "00"] }
    ];

    let combosTerno = [];
    let combosDuque = [];

    function popularSelects() {
      const selectsTerno = ["t_grupo1", "t_grupo2", "t_grupo3"];
      selectsTerno.forEach(function(selId, index) {
        const select = document.getElementById(selId);
        grupos.forEach(function(g) {
          const option = document.createElement("option");
          option.value = g.id;
          option.textContent = g.nome + " (" + g.dezenas.join(", ") + ")";
          select.appendChild(option);
        });
        select.value = index + 1;
      });

      const selectsDuque = ["d_grupo1", "d_grupo2"];
      selectsDuque.forEach(function(selId, index) {
        const select = document.getElementById(selId);
        grupos.forEach(function(g) {
          const option = document.createElement("option");
          option.value = g.id;
          option.textContent = g.nome + " (" + g.dezenas.join(", ") + ")";
          select.appendChild(option);
        });
        select.value = index + 1;
      });
    }

    function mudarAba(aba) {
      const abaTerno = document.getElementById("abaTerno");
      const abaDuque = document.getElementById("abaDuque");
      const btnTerno = document.getElementById("tabBtnTerno");
      const btnDuque = document.getElementById("tabBtnDuque");
      const subtitulo = document.getElementById("subtituloHeader");

      if (aba === "terno") {
        abaTerno.classList.remove("hidden");
        abaDuque.classList.add("hidden");
        btnTerno.classList.add("active");
        btnDuque.classList.remove("active");
        subtitulo.textContent = "Terno: 3 Grupos • 64 Combinações";
      } else {
        abaTerno.classList.add("hidden");
        abaDuque.classList.remove("hidden");
        btnTerno.classList.remove("active");
        btnDuque.classList.add("active");
        subtitulo.textContent = "Duque: 2 Grupos • 16 Combinações (100%)";
      }
    }

    function gerarTerno() {
      const id1 = parseInt(document.getElementById("t_grupo1").value);
      const id2 = parseInt(document.getElementById("t_grupo2").value);
      const id3 = parseInt(document.getElementById("t_grupo3").value);
      const erroMsg = document.getElementById("t_erroMsg");

      if (id1 === id2 || id1 === id3 || id2 === id3) {
        erroMsg.style.display = "block";
        document.getElementById("t_resultadoCard").classList.add("hidden");
        return;
      }

      erroMsg.style.display = "none";

      const g1 = grupos.find(function(g) { return g.id === id1; }).dezenas;
      const g2 = grupos.find(function(g) { return g.id === id2; }).dezenas;
      const g3 = grupos.find(function(g) { return g.id === id3; }).dezenas;

      combosTerno = [];

      for (let d1 of g1) {
        for (let d2 of g2) {
          for (let d3 of g3) {
            combosTerno.push(d1 + "-" + d2 + "-" + d3);
          }
        }
      }

      atualizarFinanceiro("terno", 64);
      renderizarLista("t_listaCombinacoes", combosTerno);
      document.getElementById("t_resultadoCard").classList.remove("hidden");
    }

    function gerarDuque() {
      const id1 = parseInt(document.getElementById("d_grupo1").value);
      const id2 = parseInt(document.getElementById("d_grupo2").value);
      const erroMsg = document.getElementById("d_erroMsg");

      if (id1 === id2) {
        erroMsg.style.display = "block";
        document.getElementById("d_resultadoCard").classList.add("hidden");
        return;
      }

      erroMsg.style.display = "none";

      const g1 = grupos.find(function(g) { return g.id === id1; }).dezenas;
      const g2 = grupos.find(function(g) { return g.id === id2; }).dezenas;

      combosDuque = [];

      for (let d1 of g1) {
        for (let d2 of g2) {
          combosDuque.push(d1 + "-" + d2);
        }
      }

      atualizarFinanceiro("duque", 16);
      renderizarLista("d_listaCombinacoes", combosDuque);
      document.getElementById("d_resultadoCard").classList.remove("hidden");
    }


    function atualizarFinanceiro(tipo, qtdJogos) {
      const prefixo = tipo === "terno" ? "t_" : "d_";
      const total = parseFloat(document.getElementById(prefixo + "valorTotal").value) || 0;
      const cotacao = parseFloat(document.getElementById(prefixo + "cotacao").value) || 0;

      const porJogo = total / qtdJogos;
      const retorno = porJogo * cotacao;

      document.getElementById(prefixo + "valorPorJogo").textContent = porJogo.toLocaleString("pt-BR", {
        style: "currency",
        currency: "BRL"
      });

      document.getElementById(prefixo + "retornoEstimado").textContent = retorno.toLocaleString("pt-BR", {
        style: "currency",
        currency: "BRL"
      });
    }

    function renderizarLista(containerId, lista) {
      const container = document.getElementById(containerId);
      container.innerHTML = "";

      lista.forEach(function(combo) {
        const div = document.createElement("div");
        div.className = "combo-item";
        div.textContent = combo;
        container.appendChild(div);
      });
    }

      function copiarJogos(tipo) {
      const lista = tipo === "terno" ? combosTerno : combosDuque;
      const btnId = tipo === "terno" ? "t_btnCopiar" : "d_btnCopiar";
      const texto = lista.join(String.fromCharCode(10));
      const btn = document.getElementById(btnId);
      const textoOriginal = btn.textContent;

      function mostrarSucesso() {
        btn.textContent = "Copiado com sucesso!";
        btn.style.background = "#10b981";
        setTimeout(function() {
          btn.textContent = textoOriginal;
          btn.style.background = "#3b82f6";
        }, 2000);
      }

      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(texto).then(mostrarSucesso).catch(function() {
          copiarFallback(texto, mostrarSucesso);
        });
      } else {
        copiarFallback(texto, mostrarSucesso);
      }
    }

    function copiarFallback(texto, callback) {
      const area = document.createElement("textarea");
      area.value = texto;
      area.style.position = "fixed";
      area.style.left = "-9999px";
      document.body.appendChild(area);
      area.focus();
      area.select();
      try {
        document.execCommand("copy");
        callback();
      } catch (err) {
        alert("Não foi possível copiar automaticamente. Selecione os números na tela.");
      }
      document.body.removeChild(area);
    }

    document.addEventListener("DOMContentLoaded", function() {
      popularSelects();
    });
  </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_APP)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
