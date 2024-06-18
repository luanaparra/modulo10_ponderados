import 'package:flutter/material.dart';
import 'login.dart';
import 'sign.dart';
import 'screenshot.dart';
import 'upload_image.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'My App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      initialRoute: '/',
      routes: {
        '/': (context) => Login(),
        '/signup': (context) => SignUp(),
        '/screenshot': (context) => Screenshot(),
        '/upload': (context) => UploadImage(),
      },
    );
  }
}
