# Space Shooter
### A Space Invaders game built with Python, featuring player and score tracking.

###------Deliverables------

Spaceship moves horizontally and shoots bullets upward to destroy alien invaders.
Aliens move in a grid formation and fire bullets randomly at the player.
Player has a visible health bar; losing all health triggers Game Over.
Scores are saved persistently per player in a CSV file.
A High Scores screen displays the Top 5 players ranked by score.
The project is modular with separate files for entities, game logic, settings, and utilities.


###------Architectural Design Decisions------

settings.py is the global config module — holds all constants, shared assets, and mutable game state (score, countdown, player_name).
entities.py is the actor module — defines all sprite classes (Spaceship, Aliens, Bullets, Alien_Bullets, Explosion, MenuButton) and all sprite groups.
game.py is the game manager — handles all screens (menu, name registration, game loop, leaderboard) and all CSV-based player persistence.
utils.py is a stateless helper module — image loading with background removal, background drawing, and text rendering.
main.py is the entry point — drives the top-level flow: Menu → Registration → Game Loop → repeat.


###------OOP Concepts and How They Are Applied------

Encapsulation: Spaceship manages its own health, draws its own health bar.
Inheritance: All game entities inherit from pygame.sprite.Sprite, gaining group management and collision detection.
Polymorphism: Every sprite class implements update(). The game loop calls it uniformly on all groups without knowing each class's internal logic.
Abstraction: game.py does not know how aliens coordinate direction flips or how explosions animate — it simply calls .update() and .draw().
Composition: The game session holds sprite groups (spaceship_group, alien_group, etc.).
