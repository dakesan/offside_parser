import streamlit as st
import pandas as pd


def main():
    st.markdown("# offside変換app")
    f_csv=st.file_uploader("translist.csvをアップロード",type='csv')
    
    if f_csv:
    
        df = pd.read_csv(f_csv,encoding='cp932')

        df_selected = df[['納品・返品完了日', '会計コード１名称', '商品名',
                        '購入額（税抜）', '納品・返品完了数量', 'バイヤユーザ名']]
        df_selected.columns = ["納品日", "テーマ番号", "品名", "単価", "個数", "購入者"]
        df_selected.replace("'", "", regex=True, inplace=True)

        df_selected['月'] = [string[4:6] for string in df_selected['納品日']]
        df_selected['日'] = [string[6:] for string in df_selected['納品日']]

        df_selected

        @st.cache
        def convert_df(df):
            return df.to_csv().encode('shift_jis')
        
        xl = convert_df(df_selected)
        
        st.download_button(
            "パース結果をダウンロード（excel）",
            xl,
            "file.csv",
            "text/csv",
            key='download-csv'
        )
    else:
        pass
    
if __name__ == '__main__':
    main()
