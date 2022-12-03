import 'package:flame/components.dart';
import 'package:flame/game.dart';
import 'package:flame/input.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(
    GameWidget(
      game: MyGame(),
    ),
  );
}

/// This example simply adds a rotating white square on the screen.
/// If you press on a square, it will be removed.
/// If you press anywhere else, another square will be added.
class MyGame extends FlameGame with HasTappables {
  SpriteComponent bunny = SpriteComponent();
  SpriteComponent background = SpriteComponent();

  @override
  Future<void> onLoad() async {
    // super.onLoad();
    // print("loaded");
    background.sprite = await loadSprite('background.png');
    background.size = size * 4;
    // background.y = size[1];
    background.x = 0;
    background.y = -size[1] * 3;
    add(background);

    bunny.sprite = await loadSprite('bunny.png');
    bunny.width = 100;
    bunny.height = 100;
    bunny.y = size[1] - 100;
    bunny.x = size[0] / 2 - 50;
    add(bunny);
  }

  @override
  void onTapDown(int id, TapDownInfo info) {
    super.onTapDown(id, info);

    final touchPoint = info.eventPosition.game;
    if (touchPoint.x < size[0] / 2 - 30) {
      if (background.x < 0) {
        background.x += 10;
      }
      print(background.x);
    } else if (touchPoint.x > size[0] / 2 + 30) {
      background.x -= 10;
      print(background.x);
    } else {
      if (touchPoint.y < size[1] / 2) {
        background.y += 10;
        print(background.y);
      } else if (touchPoint.y > size[1] / 2) {
        background.y -= 10;
        print(background.size);
      }
    }
  }
}

// class MovementButton extends SpriteComponent with Tappable {
//   @override
//   bool onTapDown(TapDownInfo info) {
//     try {
//       print("tapped");
//       return true;
//     } catch (e) {
//       print("error");
//       return false;
//     }
//   }
// }
