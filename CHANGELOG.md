## [0.1.0] - 2026-06-15

- Player movimentável
- Sistema de colisão
- Sistema de vitória e derrota

## [0.1.1] - 2026-06-16

- Adicionado spawn dinâmico de inimigos
- Adicionado contador de score
- Adicionado timer de sobrevivência

## [0.1.2]

- Adicionado sistema de partículas
- Adicionado animação com 9 sprites
- Adicionado flip automático do personagem

## [0.1.3] - 2026-06-17

### Adicionado

- Sistema de Parallax com 5 layers.
- Loop infinito dos backgrounds.
- Sistema de partículas para o jogador.
- Contador de inimigos na HUD.
- Fonte personalizada PressStart2P.
- Sistema de score baseado em tempo.

### Melhorado

- Animação do jogador expandida para 9 sprites.
- Sistema de direção utilizando flip horizontal.
- Separação entre inimigos para evitar sobreposição.

### Corrigido

- Problemas de orientação dos sprites.
- Bugs no sistema de partículas.
- Bugs de repetição de imagens durante o Parallax.

## [0.1.4] - 2026-06-22

- varios booleans removidos em game.py para otimizar o codigo
- funcionalidade de vida i-frames e melhora na colisão
- mudança no tamanho dos personagens
- HUD basica de vida
- sistema de knoback estilizado

## [0.1.5] - 2026-06-23

### Adicionado

- Barra de vida visual preparada para implementação.
- Configurações da barra de vida centralizadas no `settings.py`.
- Novo módulo `render.py` para centralizar toda a renderização do jogo.

### Refatorado

- Sistema completo de renderização separado do `game.py`.
- Renderização organizada em funções específicas:
  - `draw_background()`
  - `draw_trails()`
  - `draw_game_state()`
  - `draw_hud()`
- Camera Shake integrado ao sistema de renderização.
- HUD reorganizada para facilitar futuras expansões.
- Código do `draw()` simplificado, tornando a leitura e manutenção mais fáceis.

### Melhorado

- Organização geral do projeto.
- Separação de responsabilidades entre lógica do jogo e renderização.
- Estrutura preparada para futuras habilidades, efeitos visuais e expansão do projeto.

## [0.1.6] - 2026-06-27

### Adicionado

- Barra de vida visual totalmente funcional.
- Animação suave da barra de vida utilizando Interpolação Linear (LERP).
- Novo módulo `utils.py` para centralizar funções utilitárias reutilizáveis.
- Primeira função utilitária do projeto: `lerp()`.
- Novo estado visual `display_health`, separado da vida real do jogador.
- Estrutura inicial do sistema de habilidades com a criação da pasta `skills/`.

### Refatorado

- Sistema de atualização do `Player` reorganizado através do método `Player.update()`.
- Atualização da invencibilidade integrada ao fluxo de atualização do jogador.
- Sistema preparado para futuras atualizações do Player sem aumentar o acoplamento com o `Game`.
- Organização da HUD simplificada, incorporando a barra de vida ao próprio sistema de interface.

### Melhorado

- Separação entre estado lógico (`health`) e representação visual (`display_health`), permitindo animações independentes da lógica do jogo.
- Arquitetura preparada para reutilização da interpolação em futuras habilidades, barras e efeitos visuais.
- Organização do projeto visando maior escalabilidade para o futuro sistema de habilidades.
- Estrutura do código mais modular, reduzindo dependências entre classes.

### Corrigido

- Removido código morto relacionado ao sistema de invencibilidade durante a refatoração do `Player`.
- Ajustes na posição e renderização da barra de vida na HUD.
