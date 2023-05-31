import { NavigationContainer } from "@react-navigation/native";

//Stack에서 작동하는 Navigator와 Screen를 위해 함수 추가
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";

//네비게이션에서 사용할 화면 가져오기
//여기서 화면은 우리가 흔히 볼 수 있는 컴포넌트 이다.
import { Join } from "./Mypage";

//Stack Navigation만들기
const Tab = createBottomTabNavigator();

const LoginNavigation = ({}) => {
  <NavigationContainer>
    <Tab.Navigator>
      <Tab.Screen
        name="Mypage"
        component={Join}
        options={{
          tabBarVisible: false,
        }}
      />
      <Tab.Screen name="Join2" component={Join} />
    </Tab.Navigator>
  </NavigationContainer>;
};

export default LoginNavigation;
