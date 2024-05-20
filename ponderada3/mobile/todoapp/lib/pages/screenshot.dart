import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:screenshot/screenshot.dart';
import 'package:gallery_saver/gallery_saver.dart';

class Screenshot extends StatelessWidget {
  final ScreenshotController _screenshotController = ScreenshotController();

  Future<void> _captureScreenshot() async {
    final Uint8List? screenshot = await _screenshotController.capture();

    if (screenshot != null) {
      final bool? result = await GallerySaver.saveImage(
        screenshot,
        albumName: 'Screenshots',
      );
      if (result != null && result) {
        print('Captura de tela salva na galeria');
      } else {
        print('Falha ao salvar a captura de tela');
      }
    } else {
      print('Falha ao capturar a tela');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Captura de Tela'),
      ),
      body: Screenshot(
        controller: _screenshotController,
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Text('Esta é a tela de captura de tela.'),
              SizedBox(height: 16.0),
              ElevatedButton(
                onPressed: _captureScreenshot,
                child: Text('Capturar Tela'),
              ),
              SizedBox(height: 16.0),
              ElevatedButton(
                onPressed: () {
                  Navigator.of(context).pop();
                },
                child: Text('Voltar'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
