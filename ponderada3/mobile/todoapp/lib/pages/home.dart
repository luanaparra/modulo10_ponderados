import 'package:flutter/material.dart';
import 'todo_list_screen.dart';

class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Welcome'),
      ),
      body: Center(
        child: ElevatedButton(
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => Tasks()),
            );
          },
          child: Text('Go to Todo List'),
        ),
      ),
    );
  }
}