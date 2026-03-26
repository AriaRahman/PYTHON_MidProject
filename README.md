<h1 align="center">🚀 Space Shooter Game</h1>
<p align="center">A classic Space Invaders  game built with <strong>Python & Pygame</strong>, featuring player registration and persistent score tracking.</p>

Deliverables

✅ Spaceship moves horizontally and shoots bullets upward to destroy alien invaders
✅ Aliens move in a grid formation and fire bullets randomly at the player
✅ Player has a visible health bar; losing all health triggers Game Over
✅ Scores are saved persistently per player in a CSV file
✅ A High Scores screen displays the Top 5 players ranked by score [Implementation isn't done yet]
✅ The project is modular with separate files for entities, game logic, settings, and utilities


<h2> Architectural Design Decisions</h2>

settings.py — Global config module; holds all constants, shared assets, and mutable game state (score, countdown, player_name)
entities.py — Actor module; defines all sprite classes (Spaceship, Aliens, Bullets, Alien_Bullets, Explosion, MenuButton) and all sprite groups
game.py — Game manager; handles all screens (menu, name registration, game loop, leaderboard) and all CSV-based player persistence
utils.py — Stateless helper module; image loading with background removal, background drawing, and text rendering
main.py — Entry point; drives the top-level flow: Menu → Registration → Game Loop → repeat


<h2>OOP Concepts and How They Are Applied</h2>

Encapsulation: Spaceship manages its own health and draws its own health bar — the game manager never modifies health directly
Inheritance: All game entities inherit from pygame.sprite.Sprite, gaining group management and collision detection
Polymorphism: Every sprite class implements update() — the game loop calls it uniformly on all groups without knowing each class's internal logic
Abstraction: game.py does not know how aliens coordinate direction flips or how explosions animate — it simply calls .update() and .draw()
Composition: The game session holds sprite groups (spaceship_group, alien_group, etc.), showing a clear HAS-A relationship
