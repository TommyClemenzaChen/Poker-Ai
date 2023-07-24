import * as React from "react";
import {Image, StyleSheet, Pressable, Text, View} from "react-native";
import {useNavigation} from "@react-navigation/native";
import { FontFamily, Padding, Color, FontSize } from "./GlobalStyles";

const Result = () => {
  	const navigation = useNavigation();
  	
  	return (
    		<Pressable style={[styles.result, styles.iconLayout]} onPress={()=>{}}>
      			<View style={styles.header}>
        				<Pressable style={[styles.back1, styles.backLayout]} onPress={()=>{}}>
          					<Image style={[styles.icon, styles.iconLayout]} resizeMode="cover" source="back.png" />
        				</Pressable>
        				<View style={[styles.textHereWrapper, styles.wrapperFlexBox]}>
          					<Text style={[styles.textHere2, styles.foldTypo]}>Result</Text>
        				</View>
        				<View style={[styles.back2, styles.backLayout]} />
      			</View>
      			<View style={[styles.frameParent, styles.buttonFlexBox]}>
        				<View style={[styles.frameWrapper, styles.wrapperFlexBox]}>
          					<View style={styles.foldWrapper}>
            						<Text style={[styles.fold, styles.foldTypo]}>Fold</Text>
          					</View>
        				</View>
        				<View style={[styles.emoji, styles.emojiSpaceBlock]}>
          					<Image style={[styles.emojiChild, styles.emojiLayout]} resizeMode="cover" source="Polygon 1.png" />
          					<Image style={[styles.emojiItem, styles.emojiItemPosition]} resizeMode="cover" source="Polygon 2.png" />
          					<View style={[styles.vectorParent, styles.emojiItemPosition]}>
            						<Image style={[styles.vectorIcon, styles.vectorIconLayout]} resizeMode="cover" source="Vector.png" />
            						<Image style={[styles.vectorIcon1, styles.vectorIconLayout]} resizeMode="cover" source="Vector.png" />
            						<Image style={styles.frameChild} resizeMode="cover" source="Line 4.png" />
          					</View>
        				</View>
        				<Pressable style={[styles.button, styles.emojiSpaceBlock]} onPress={()=>{}}>
          					<Text style={styles.textHere3}>View Details</Text>
        				</Pressable>
      			</View>
    		</Pressable>);
};

const styles = StyleSheet.create({
  	iconLayout: {
    		width: "100%",
    		overflow: "hidden"
  	},
  	backLayout: {
    		width: 48,
    		height: 48
  	},
  	wrapperFlexBox: {
    		justifyContent: "center",
    		alignItems: "center"
  	},
  	foldTypo: {
    		fontFamily: FontFamily.plusJakartaSansBold,
    		fontWeight: "700",
    		textAlign: "left"
  	},
  	buttonFlexBox: {
    		paddingHorizontal: Padding.p_41xl,
    		justifyContent: "center",
    		alignItems: "center"
  	},
  	emojiSpaceBlock: {
    		marginTop: 60,
    		overflow: "hidden"
  	},
  	emojiLayout: {
    		height: 79,
    		width: 22
  	},
  	emojiItemPosition: {
    		top: 91,
    		position: "absolute"
  	},
  	vectorIconLayout: {
    		height: 93,
    		width: 40
  	},
  	icon: {
    		height: "100%",
    		overflow: "hidden"
  	},
  	back1: {
    		height: 48
  	},
  	textHere2: {
    		color: Color.whitesmoke,
    		textAlign: "left",
    		fontSize: FontSize.size_lg
  	},
  	textHereWrapper: {
    		height: 48,
    		flexDirection: "row"
  	},
  	back2: {
    		height: 48,
    		overflow: "hidden"
  	},
  	header: {
    		borderColor: "#606060",
    		borderBottomWidth: 0.5,
    		width: 390,
    		height: 90,
    		alignItems: "flex-end",
    		justifyContent: "space-between",
    		flexDirection: "row",
    		borderStyle: "solid",
    		overflow: "hidden",
    		backgroundColor: Color.gray
  	},
  	fold: {
    		fontSize: 44,
    		color: Color.burlywood,
    		textAlign: "left"
  	},
  	foldWrapper: {
    		flexDirection: "row",
    		alignItems: "center"
  	},
  	frameWrapper: {
    		alignSelf: "stretch"
  	},
  	emojiChild: {
    		top: 90,
    		left: 50,
    		position: "absolute"
  	},
  	emojiItem: {
    		left: 108,
    		height: 79,
    		width: 22
  	},
  	vectorIcon: {
    		zIndex: 0
  	},
  	vectorIcon1: {
    		zIndex: 1,
    		marginLeft: 30
  	},
  	frameChild: {
    		top: 25,
    		left: 35,
    		width: 24,
    		height: 11,
    		zIndex: 2,
    		position: "absolute"
  	},
  	vectorParent: {
    		marginLeft: -47,
    		left: "50%",
    		flexDirection: "row"
  	},
  	emoji: {
    		borderRadius: 100,
    		backgroundColor: Color.whitesmoke,
    		borderColor: "#252525",
    		borderWidth: 8,
    		width: 180,
    		height: 180,
    		borderStyle: "solid"
  	},
  	textHere3: {
    		fontWeight: "800",
    		fontFamily: FontFamily.plusJakartaSansExtrabold,
    		color: Color.gray,
    		textAlign: "left",
    		fontSize: FontSize.size_lg
  	},
  	button: {
    		borderRadius: 30,
    		backgroundColor: Color.burlywood,
    		height: 60,
    		paddingVertical: 10,
    		paddingHorizontal: Padding.p_41xl,
    		justifyContent: "center",
    		alignItems: "center",
    		flexDirection: "row"
  	},
  	frameParent: {
    		paddingVertical: 80,
    		alignSelf: "stretch",
    		flex: 1
  	},
  	result: {
    		height: 844,
    		alignItems: "center",
    		overflow: "hidden",
    		flex: 1,
    		backgroundColor: Color.gray
  	}
});

export default Result;
