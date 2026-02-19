const C3 = self.C3;
self.C3_GetObjectRefTable = function () {
	return [
		C3.Plugins.Text,
		C3.Plugins.Sprite,
		C3.Plugins.Button,
		C3.Plugins.TextBox,
		C3.Plugins.List,
		C3.Plugins.Arr,
		C3.Plugins.Button.Cnds.OnClicked,
		C3.Plugins.System.Acts.SetVar,
		C3.Plugins.System.Acts.GoToLayout,
		C3.Plugins.System.Cnds.OnLayoutStart,
		C3.Plugins.Text.Acts.SetText,
		C3.Plugins.Arr.Acts.Push,
		C3.Plugins.System.Exps.uppercase,
		C3.Plugins.TextBox.Exps.Text,
		C3.Plugins.List.Acts.Clear,
		C3.Plugins.System.Cnds.Repeat,
		C3.Plugins.Arr.Exps.Width,
		C3.Plugins.List.Acts.AddItem,
		C3.Plugins.Arr.Exps.At,
		C3.Plugins.System.Exps.loopindex
	];
};
self.C3_JsPropNameTable = [
	{TextTitle: 0},
	{TextInstructions: 0},
	{SpriteRespect: 0},
	{SpriteIntegrity: 0},
	{SpriteInclusion: 0},
	{SpriteCourage: 0},
	{ButtonIntegrity: 0},
	{ButtonCourage: 0},
	{ButtonRespect: 0},
	{ButtonInclusion: 0},
	{TextInput: 0},
	{ButtonSave: 0},
	{List: 0},
	{ButtonCelebrate: 0},
	{ArrayJournal: 0},
	{CurrentValue: 0}
];

self.InstanceType = {
	TextTitle: class extends self.ITextInstance {},
	TextInstructions: class extends self.ITextInstance {},
	SpriteRespect: class extends self.ISpriteInstance {},
	SpriteIntegrity: class extends self.ISpriteInstance {},
	SpriteInclusion: class extends self.ISpriteInstance {},
	SpriteCourage: class extends self.ISpriteInstance {},
	ButtonIntegrity: class extends self.IButtonInstance {},
	ButtonCourage: class extends self.IButtonInstance {},
	ButtonRespect: class extends self.IButtonInstance {},
	ButtonInclusion: class extends self.IButtonInstance {},
	TextInput: class extends self.ITextInputInstance {},
	ButtonSave: class extends self.IButtonInstance {},
	List: class extends self.IListInstance {},
	ButtonCelebrate: class extends self.IButtonInstance {},
	ArrayJournal: class extends self.IArrayInstance {}
}