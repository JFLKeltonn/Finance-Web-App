import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class NewsView extends StatelessWidget {
  const NewsView({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text('News Screen'),
        ),
        body: Center(
            child: ElevatedButton(
          onPressed: () => context.go('/home'),
          child: Text('Route to Home Page'),
        )));
  }
}
