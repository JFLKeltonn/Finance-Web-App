import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class LoadingView extends StatelessWidget {
  const LoadingView({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
      title: const Text('Loading Screen'),
    ));
  }
}
