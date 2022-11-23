import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'routes/HomeView.dart';
import 'routes/LoadingView.dart';
import 'routes/NewsView.dart';

void main() {
  runApp(MyApp());
}

final GoRouter _router = GoRouter(routes: [
  GoRoute(
    path: '/',
    builder: (context, state) => const LoadingView(),
  ),
  GoRoute(
    path: '/home',
    builder: (context, state) => const HomeView(),
  ),
  GoRoute(
    path: '/news',
    builder: (context, state) => const NewsView(),
  ),
]);

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      title: 'Finance Application',
      theme: ThemeData.dark(),
      routerConfig: _router,
    );
  }
}
