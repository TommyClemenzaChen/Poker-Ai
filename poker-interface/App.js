import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import StarterPage from './starter';
import customInput from './study';
import ResultPage from './result';
import {NavigationContainer} from "@react-navigation/native"
 const Stack = createStackNavigator();

export default function App() {
  return (
  <NavigationContainer>
    <Stack.Navigator>
      <Stack.Screen
        name="StarterPage"
        component={StarterPage}
        options={{ headerShown: false }}
      />
      <Stack.Screen
        name="StudyPage"
        component={customInput}
        options={{ headerShown: false }}
      />
      <Stack.Screen
        name="ResultPage"
        component={ResultPage}
        options={{ headerShown: false }}
      />
    </Stack.Navigator>
    </NavigationContainer>
  );
};

