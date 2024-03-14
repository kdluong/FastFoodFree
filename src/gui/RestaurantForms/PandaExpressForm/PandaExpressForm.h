//---------------------------------------------------------------------------

#ifndef PandaExpressFormH
#define PandaExpressFormH
//---------------------------------------------------------------------------
#include <System.Classes.hpp>
#include <FMX.Controls.hpp>
#include <FMX.Forms.hpp>
#include <FMX.Controls.Presentation.hpp>
#include <FMX.StdCtrls.hpp>
#include <FMX.Types.hpp>
#include <FMX.Edit.hpp>
#include <Data.Bind.Components.hpp>
#include <Data.Bind.ObjectScope.hpp>
#include <REST.Client.hpp>
#include <REST.Types.hpp>
//---------------------------------------------------------------------------
class TMyPandaExpressForm : public TForm
{
__published:	// IDE-managed Components
	TLabel *PandaExpressLabel;
	TLabel *SurveyCodeLabel;
	TLabel *RatingLabel;
	TButton *SubmitButton;
	TEdit *EmailEdit;
	TEdit *Code1Edit;
	TEdit *Code2Edit;
	TEdit *Code3Edit;
	TEdit *Code4Edit;
	TEdit *Code5Edit;
	TEdit *Code6Edit;
	TLabel *InfoLabel;
	TRadioButton *DineInButton;
	TRadioButton *PickUpButton;
	TRadioButton *DeliveryButton;
	TRadioButton *Rating1Button;
	TRadioButton *Rating3Button;
	TRadioButton *Rating4Button;
	TRadioButton *Rating5Button;
	TButton *BackButton;
	TRadioButton *Rating2Button;
	TLabel *Label1;
	TRESTRequest *RESTRequest1;
	TRESTResponse *RESTResponse1;
	TRESTClient *RESTClient1;
	void __fastcall BackButtonClick(TObject *Sender);
	void __fastcall SubmitButtonClick(TObject *Sender);
	void __fastcall RESTRequest1AfterExecute(TCustomRESTRequest *Sender);
private:	// User declarations
	bool ValidCode(std::string value, int maxLength);
	bool ValidEmail(std::string email);
    void ToggleEnabled();
public:		// User declarations
	__fastcall TMyPandaExpressForm(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TMyPandaExpressForm *MyPandaExpressForm;
//---------------------------------------------------------------------------
#endif
