# kbo 홈페이지
html = """
<table class="tData" cellspacing="0" cellpadding="0" summary="날짜,요일,홈,방문,구장,관중수,">
					<caption>경기 관중 현황</caption>
					<colgroup>
						<col width="16%">
						<col width="16%">
						<col width="16%">
						<col width="16%">
						<col width="16%">
						<col width="*">
					</colgroup>
					<thead>
						<tr>
							<th scope="col">날짜</th>
							<th scope="col">요일</th>
							<th scope="col">홈</th>
							<th scope="col">방문</th>
							<th scope="col">구장</th>
							<th scope="col">관중수</th>
						</tr>
					</thead>
					<tfoot>
						<tr class="total">
							<td colspan="6">
								<ul>
									<li><strong>경기수 : <span id="cphContents_cphContents_cphContents_lblGameCount">720</span></strong> </li>
									<li><strong>경기평균 : <span id="cphContents_cphContents_cphContents_lblCrowdAvg">11,250</span></strong> </li>
									<li><strong>경기 합계 : <span id="cphContents_cphContents_cphContents_lblCrowdSum">8,100,326</span></strong></li>
								</ul>
							</td>
						</tr>
					</tfoot>
					<tbody>
						
							<tr class="order">
								<td>2023/04/01</td>
								<td>토</td>
								<td>키움</td>
								<td>한화</td>
								<td>고척</td>
								<td>16,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/01</td>
								<td>토</td>
								<td>SSG</td>
								<td>KIA</td>
								<td>문학</td>
								<td>23,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/01</td>
								<td>토</td>
								<td>KT</td>
								<td>LG</td>
								<td>수원</td>
								<td>18,700</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/01</td>
								<td>토</td>
								<td>두산</td>
								<td>롯데</td>
								<td>잠실</td>
								<td>23,750</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/01</td>
								<td>토</td>
								<td>삼성</td>
								<td>NC</td>
								<td>대구</td>
								<td>24,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/02</td>
								<td>일</td>
								<td>키움</td>
								<td>한화</td>
								<td>고척</td>
								<td>11,562</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/02</td>
								<td>일</td>
								<td>SSG</td>
								<td>KIA</td>
								<td>문학</td>
								<td>23,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/02</td>
								<td>일</td>
								<td>KT</td>
								<td>LG</td>
								<td>수원</td>
								<td>14,700</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/02</td>
								<td>일</td>
								<td>두산</td>
								<td>롯데</td>
								<td>잠실</td>
								<td>23,750</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/02</td>
								<td>일</td>
								<td>삼성</td>
								<td>NC</td>
								<td>대구</td>
								<td>18,483</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/04</td>
								<td>화</td>
								<td>삼성</td>
								<td>한화</td>
								<td>대구</td>
								<td>5,936</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/04</td>
								<td>화</td>
								<td>키움</td>
								<td>LG</td>
								<td>고척</td>
								<td>4,510</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/04</td>
								<td>화</td>
								<td>SSG</td>
								<td>롯데</td>
								<td>문학</td>
								<td>5,809</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/04</td>
								<td>화</td>
								<td>두산</td>
								<td>NC</td>
								<td>잠실</td>
								<td>3,924</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/05</td>
								<td>수</td>
								<td>키움</td>
								<td>LG</td>
								<td>고척</td>
								<td>4,194</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/05</td>
								<td>수</td>
								<td>두산</td>
								<td>NC</td>
								<td>잠실</td>
								<td>2,172</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/06</td>
								<td>목</td>
								<td>삼성</td>
								<td>한화</td>
								<td>대구</td>
								<td>6,525</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/06</td>
								<td>목</td>
								<td>키움</td>
								<td>LG</td>
								<td>고척</td>
								<td>4,556</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/06</td>
								<td>목</td>
								<td>두산</td>
								<td>NC</td>
								<td>잠실</td>
								<td>3,724</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/07</td>
								<td>금</td>
								<td>롯데</td>
								<td>KT</td>
								<td>사직</td>
								<td>14,734</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/07</td>
								<td>금</td>
								<td>KIA</td>
								<td>두산</td>
								<td>광주</td>
								<td>12,821</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/07</td>
								<td>금</td>
								<td>한화</td>
								<td>SSG</td>
								<td>대전</td>
								<td>10,415</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/07</td>
								<td>금</td>
								<td>LG</td>
								<td>삼성</td>
								<td>잠실</td>
								<td>17,201</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/07</td>
								<td>금</td>
								<td>NC</td>
								<td>키움</td>
								<td>창원</td>
								<td>6,867</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/08</td>
								<td>토</td>
								<td>롯데</td>
								<td>KT</td>
								<td>사직</td>
								<td>16,555</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/08</td>
								<td>토</td>
								<td>KIA</td>
								<td>두산</td>
								<td>광주</td>
								<td>16,432</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/08</td>
								<td>토</td>
								<td>한화</td>
								<td>SSG</td>
								<td>대전</td>
								<td>11,232</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/08</td>
								<td>토</td>
								<td>LG</td>
								<td>삼성</td>
								<td>잠실</td>
								<td>22,141</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/08</td>
								<td>토</td>
								<td>NC</td>
								<td>키움</td>
								<td>창원</td>
								<td>9,763</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/09</td>
								<td>일</td>
								<td>롯데</td>
								<td>KT</td>
								<td>사직</td>
								<td>12,283</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/09</td>
								<td>일</td>
								<td>KIA</td>
								<td>두산</td>
								<td>광주</td>
								<td>14,070</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/09</td>
								<td>일</td>
								<td>한화</td>
								<td>SSG</td>
								<td>대전</td>
								<td>9,455</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/09</td>
								<td>일</td>
								<td>LG</td>
								<td>삼성</td>
								<td>잠실</td>
								<td>20,439</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/09</td>
								<td>일</td>
								<td>NC</td>
								<td>키움</td>
								<td>창원</td>
								<td>7,686</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/11</td>
								<td>화</td>
								<td>KIA</td>
								<td>한화</td>
								<td>광주</td>
								<td>3,623</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/11</td>
								<td>화</td>
								<td>NC</td>
								<td>KT</td>
								<td>창원</td>
								<td>2,069</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/11</td>
								<td>화</td>
								<td>롯데</td>
								<td>LG</td>
								<td>사직</td>
								<td>5,286</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/11</td>
								<td>화</td>
								<td>삼성</td>
								<td>SSG</td>
								<td>대구</td>
								<td>3,907</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/11</td>
								<td>화</td>
								<td>두산</td>
								<td>키움</td>
								<td>잠실</td>
								<td>4,372</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/12</td>
								<td>수</td>
								<td>KIA</td>
								<td>한화</td>
								<td>광주</td>
								<td>5,252</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/12</td>
								<td>수</td>
								<td>NC</td>
								<td>KT</td>
								<td>창원</td>
								<td>2,448</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/12</td>
								<td>수</td>
								<td>롯데</td>
								<td>LG</td>
								<td>사직</td>
								<td>6,519</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/12</td>
								<td>수</td>
								<td>삼성</td>
								<td>SSG</td>
								<td>대구</td>
								<td>5,405</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/13</td>
								<td>목</td>
								<td>KIA</td>
								<td>한화</td>
								<td>광주</td>
								<td>5,457</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/13</td>
								<td>목</td>
								<td>NC</td>
								<td>KT</td>
								<td>창원</td>
								<td>3,174</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/13</td>
								<td>목</td>
								<td>롯데</td>
								<td>LG</td>
								<td>사직</td>
								<td>6,505</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/13</td>
								<td>목</td>
								<td>삼성</td>
								<td>SSG</td>
								<td>대구</td>
								<td>4,648</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/13</td>
								<td>목</td>
								<td>두산</td>
								<td>키움</td>
								<td>잠실</td>
								<td>6,917</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/14</td>
								<td>금</td>
								<td>KT</td>
								<td>한화</td>
								<td>수원</td>
								<td>7,145</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/14</td>
								<td>금</td>
								<td>키움</td>
								<td>KIA</td>
								<td>고척</td>
								<td>8,043</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/14</td>
								<td>금</td>
								<td>삼성</td>
								<td>롯데</td>
								<td>대구</td>
								<td>9,124</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/14</td>
								<td>금</td>
								<td>SSG</td>
								<td>NC</td>
								<td>문학</td>
								<td>8,218</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/14</td>
								<td>금</td>
								<td>LG</td>
								<td>두산</td>
								<td>잠실</td>
								<td>16,528</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/15</td>
								<td>토</td>
								<td>KT</td>
								<td>한화</td>
								<td>수원</td>
								<td>13,212</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/15</td>
								<td>토</td>
								<td>키움</td>
								<td>KIA</td>
								<td>고척</td>
								<td>13,752</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/15</td>
								<td>토</td>
								<td>삼성</td>
								<td>롯데</td>
								<td>대구</td>
								<td>18,231</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/15</td>
								<td>토</td>
								<td>SSG</td>
								<td>NC</td>
								<td>문학</td>
								<td>13,956</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/15</td>
								<td>토</td>
								<td>LG</td>
								<td>두산</td>
								<td>잠실</td>
								<td>21,243</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/16</td>
								<td>일</td>
								<td>KT</td>
								<td>한화</td>
								<td>수원</td>
								<td>13,010</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/16</td>
								<td>일</td>
								<td>키움</td>
								<td>KIA</td>
								<td>고척</td>
								<td>11,265</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/16</td>
								<td>일</td>
								<td>삼성</td>
								<td>롯데</td>
								<td>대구</td>
								<td>16,076</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/16</td>
								<td>일</td>
								<td>SSG</td>
								<td>NC</td>
								<td>문학</td>
								<td>13,460</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/16</td>
								<td>일</td>
								<td>LG</td>
								<td>두산</td>
								<td>잠실</td>
								<td>20,090</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/18</td>
								<td>화</td>
								<td>롯데</td>
								<td>KIA</td>
								<td>사직</td>
								<td>3,829</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/18</td>
								<td>화</td>
								<td>LG</td>
								<td>NC</td>
								<td>잠실</td>
								<td>6,574</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/18</td>
								<td>화</td>
								<td>한화</td>
								<td>두산</td>
								<td>대전</td>
								<td>4,012</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/18</td>
								<td>화</td>
								<td>KT</td>
								<td>SSG</td>
								<td>수원</td>
								<td>3,398</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/18</td>
								<td>화</td>
								<td>키움</td>
								<td>삼성</td>
								<td>고척</td>
								<td>3,104</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/19</td>
								<td>수</td>
								<td>롯데</td>
								<td>KIA</td>
								<td>사직</td>
								<td>4,869</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/19</td>
								<td>수</td>
								<td>LG</td>
								<td>NC</td>
								<td>잠실</td>
								<td>7,090</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/19</td>
								<td>수</td>
								<td>한화</td>
								<td>두산</td>
								<td>대전</td>
								<td>4,212</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/19</td>
								<td>수</td>
								<td>KT</td>
								<td>SSG</td>
								<td>수원</td>
								<td>3,405</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/19</td>
								<td>수</td>
								<td>키움</td>
								<td>삼성</td>
								<td>고척</td>
								<td>3,869</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/20</td>
								<td>목</td>
								<td>롯데</td>
								<td>KIA</td>
								<td>사직</td>
								<td>6,423</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/20</td>
								<td>목</td>
								<td>LG</td>
								<td>NC</td>
								<td>잠실</td>
								<td>9,090</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/20</td>
								<td>목</td>
								<td>한화</td>
								<td>두산</td>
								<td>대전</td>
								<td>4,122</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/20</td>
								<td>목</td>
								<td>KT</td>
								<td>SSG</td>
								<td>수원</td>
								<td>4,472</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/20</td>
								<td>목</td>
								<td>키움</td>
								<td>삼성</td>
								<td>고척</td>
								<td>3,918</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/21</td>
								<td>금</td>
								<td>두산</td>
								<td>KT</td>
								<td>잠실</td>
								<td>6,896</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/21</td>
								<td>금</td>
								<td>한화</td>
								<td>LG</td>
								<td>대전</td>
								<td>6,004</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/21</td>
								<td>금</td>
								<td>NC</td>
								<td>롯데</td>
								<td>창원</td>
								<td>12,613</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/21</td>
								<td>금</td>
								<td>KIA</td>
								<td>삼성</td>
								<td>광주</td>
								<td>6,870</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/21</td>
								<td>금</td>
								<td>SSG</td>
								<td>키움</td>
								<td>문학</td>
								<td>12,374</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/22</td>
								<td>토</td>
								<td>두산</td>
								<td>KT</td>
								<td>잠실</td>
								<td>13,410</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/22</td>
								<td>토</td>
								<td>한화</td>
								<td>LG</td>
								<td>대전</td>
								<td>11,152</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/22</td>
								<td>토</td>
								<td>NC</td>
								<td>롯데</td>
								<td>창원</td>
								<td>15,130</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/22</td>
								<td>토</td>
								<td>KIA</td>
								<td>삼성</td>
								<td>광주</td>
								<td>12,990</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/22</td>
								<td>토</td>
								<td>SSG</td>
								<td>키움</td>
								<td>문학</td>
								<td>16,535</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/23</td>
								<td>일</td>
								<td>두산</td>
								<td>KT</td>
								<td>잠실</td>
								<td>10,151</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/23</td>
								<td>일</td>
								<td>한화</td>
								<td>LG</td>
								<td>대전</td>
								<td>9,023</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/23</td>
								<td>일</td>
								<td>NC</td>
								<td>롯데</td>
								<td>창원</td>
								<td>13,286</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/23</td>
								<td>일</td>
								<td>KIA</td>
								<td>삼성</td>
								<td>광주</td>
								<td>10,026</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/23</td>
								<td>일</td>
								<td>SSG</td>
								<td>키움</td>
								<td>문학</td>
								<td>15,878</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/25</td>
								<td>화</td>
								<td>키움</td>
								<td>KT</td>
								<td>고척</td>
								<td>2,956</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/25</td>
								<td>화</td>
								<td>KIA</td>
								<td>NC</td>
								<td>광주</td>
								<td>2,216</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/25</td>
								<td>화</td>
								<td>LG</td>
								<td>SSG</td>
								<td>잠실</td>
								<td>7,344</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/26</td>
								<td>수</td>
								<td>롯데</td>
								<td>한화</td>
								<td>사직</td>
								<td>7,905</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/26</td>
								<td>수</td>
								<td>키움</td>
								<td>KT</td>
								<td>고척</td>
								<td>2,489</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/26</td>
								<td>수</td>
								<td>KIA</td>
								<td>NC</td>
								<td>광주</td>
								<td>4,798</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/26</td>
								<td>수</td>
								<td>삼성</td>
								<td>두산</td>
								<td>대구</td>
								<td>9,213</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/26</td>
								<td>수</td>
								<td>LG</td>
								<td>SSG</td>
								<td>잠실</td>
								<td>10,419</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/27</td>
								<td>목</td>
								<td>롯데</td>
								<td>한화</td>
								<td>사직</td>
								<td>10,393</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/27</td>
								<td>목</td>
								<td>키움</td>
								<td>KT</td>
								<td>고척</td>
								<td>3,024</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/27</td>
								<td>목</td>
								<td>KIA</td>
								<td>NC</td>
								<td>광주</td>
								<td>6,017</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/27</td>
								<td>목</td>
								<td>삼성</td>
								<td>두산</td>
								<td>대구</td>
								<td>8,473</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/27</td>
								<td>목</td>
								<td>LG</td>
								<td>SSG</td>
								<td>잠실</td>
								<td>13,061</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/28</td>
								<td>금</td>
								<td>LG</td>
								<td>KIA</td>
								<td>잠실</td>
								<td>22,695</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/28</td>
								<td>금</td>
								<td>한화</td>
								<td>NC</td>
								<td>대전</td>
								<td>7,242</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/28</td>
								<td>금</td>
								<td>SSG</td>
								<td>두산</td>
								<td>문학</td>
								<td>14,909</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/28</td>
								<td>금</td>
								<td>KT</td>
								<td>삼성</td>
								<td>수원</td>
								<td>7,314</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/28</td>
								<td>금</td>
								<td>롯데</td>
								<td>키움</td>
								<td>사직</td>
								<td>14,343</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/29</td>
								<td>토</td>
								<td>LG</td>
								<td>KIA</td>
								<td>잠실</td>
								<td>23,750</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/29</td>
								<td>토</td>
								<td>한화</td>
								<td>NC</td>
								<td>대전</td>
								<td>7,813</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/29</td>
								<td>토</td>
								<td>SSG</td>
								<td>두산</td>
								<td>문학</td>
								<td>20,180</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/29</td>
								<td>토</td>
								<td>KT</td>
								<td>삼성</td>
								<td>수원</td>
								<td>12,039</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/30</td>
								<td>일</td>
								<td>LG</td>
								<td>KIA</td>
								<td>잠실</td>
								<td>23,750</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/30</td>
								<td>일</td>
								<td>한화</td>
								<td>NC</td>
								<td>대전</td>
								<td>10,442</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/30</td>
								<td>일</td>
								<td>SSG</td>
								<td>두산</td>
								<td>문학</td>
								<td>21,026</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/30</td>
								<td>일</td>
								<td>KT</td>
								<td>삼성</td>
								<td>수원</td>
								<td>14,582</td>
							</tr>
						
							<tr class="order">
								<td>2023/04/30</td>
								<td>일</td>
								<td>롯데</td>
								<td>키움</td>
								<td>사직</td>
								<td>22,990</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/02</td>
								<td>화</td>
								<td>두산</td>
								<td>한화</td>
								<td>잠실</td>
								<td>9,834</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/02</td>
								<td>화</td>
								<td>SSG</td>
								<td>KT</td>
								<td>문학</td>
								<td>6,950</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/02</td>
								<td>화</td>
								<td>NC</td>
								<td>LG</td>
								<td>창원</td>
								<td>3,939</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/02</td>
								<td>화</td>
								<td>KIA</td>
								<td>롯데</td>
								<td>광주</td>
								<td>8,892</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/02</td>
								<td>화</td>
								<td>삼성</td>
								<td>키움</td>
								<td>대구</td>
								<td>10,624</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/03</td>
								<td>수</td>
								<td>두산</td>
								<td>한화</td>
								<td>잠실</td>
								<td>14,271</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/03</td>
								<td>수</td>
								<td>SSG</td>
								<td>KT</td>
								<td>문학</td>
								<td>7,703</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/03</td>
								<td>수</td>
								<td>NC</td>
								<td>LG</td>
								<td>창원</td>
								<td>4,874</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/03</td>
								<td>수</td>
								<td>KIA</td>
								<td>롯데</td>
								<td>광주</td>
								<td>13,815</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/03</td>
								<td>수</td>
								<td>삼성</td>
								<td>키움</td>
								<td>대구</td>
								<td>13,394</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/04</td>
								<td>목</td>
								<td>두산</td>
								<td>한화</td>
								<td>잠실</td>
								<td>10,825</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/04</td>
								<td>목</td>
								<td>SSG</td>
								<td>KT</td>
								<td>문학</td>
								<td>7,529</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/04</td>
								<td>목</td>
								<td>삼성</td>
								<td>키움</td>
								<td>대구</td>
								<td>12,076</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/05</td>
								<td>금</td>
								<td>키움</td>
								<td>SSG</td>
								<td>고척</td>
								<td>16,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/06</td>
								<td>토</td>
								<td>키움</td>
								<td>SSG</td>
								<td>고척</td>
								<td>11,063</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/07</td>
								<td>일</td>
								<td>한화</td>
								<td>KT</td>
								<td>대전</td>
								<td>8,551</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/07</td>
								<td>일</td>
								<td>두산</td>
								<td>LG</td>
								<td>잠실</td>
								<td>22,073</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/07</td>
								<td>일</td>
								<td>키움</td>
								<td>SSG</td>
								<td>고척</td>
								<td>7,623</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/09</td>
								<td>화</td>
								<td>KT</td>
								<td>NC</td>
								<td>수원</td>
								<td>2,764</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/09</td>
								<td>화</td>
								<td>롯데</td>
								<td>두산</td>
								<td>사직</td>
								<td>11,643</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/09</td>
								<td>화</td>
								<td>KIA</td>
								<td>SSG</td>
								<td>광주</td>
								<td>8,916</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/09</td>
								<td>화</td>
								<td>한화</td>
								<td>삼성</td>
								<td>대전</td>
								<td>5,014</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/09</td>
								<td>화</td>
								<td>LG</td>
								<td>키움</td>
								<td>잠실</td>
								<td>10,421</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/10</td>
								<td>수</td>
								<td>KT</td>
								<td>NC</td>
								<td>수원</td>
								<td>3,734</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/10</td>
								<td>수</td>
								<td>롯데</td>
								<td>두산</td>
								<td>사직</td>
								<td>11,435</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/10</td>
								<td>수</td>
								<td>KIA</td>
								<td>SSG</td>
								<td>광주</td>
								<td>8,481</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/10</td>
								<td>수</td>
								<td>한화</td>
								<td>삼성</td>
								<td>대전</td>
								<td>5,865</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/10</td>
								<td>수</td>
								<td>LG</td>
								<td>키움</td>
								<td>잠실</td>
								<td>12,125</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/11</td>
								<td>목</td>
								<td>KT</td>
								<td>NC</td>
								<td>수원</td>
								<td>3,934</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/11</td>
								<td>목</td>
								<td>롯데</td>
								<td>두산</td>
								<td>사직</td>
								<td>13,350</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/11</td>
								<td>목</td>
								<td>KIA</td>
								<td>SSG</td>
								<td>광주</td>
								<td>8,898</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/11</td>
								<td>목</td>
								<td>한화</td>
								<td>삼성</td>
								<td>대전</td>
								<td>6,007</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/11</td>
								<td>목</td>
								<td>LG</td>
								<td>키움</td>
								<td>잠실</td>
								<td>11,773</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/12</td>
								<td>금</td>
								<td>SSG</td>
								<td>한화</td>
								<td>문학</td>
								<td>14,395</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/12</td>
								<td>금</td>
								<td>두산</td>
								<td>KIA</td>
								<td>잠실</td>
								<td>20,563</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/12</td>
								<td>금</td>
								<td>삼성</td>
								<td>LG</td>
								<td>대구</td>
								<td>13,765</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/12</td>
								<td>금</td>
								<td>KT</td>
								<td>롯데</td>
								<td>수원</td>
								<td>10,937</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/12</td>
								<td>금</td>
								<td>키움</td>
								<td>NC</td>
								<td>고척</td>
								<td>3,866</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/13</td>
								<td>토</td>
								<td>SSG</td>
								<td>한화</td>
								<td>문학</td>
								<td>23,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/13</td>
								<td>토</td>
								<td>두산</td>
								<td>KIA</td>
								<td>잠실</td>
								<td>23,750</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/13</td>
								<td>토</td>
								<td>삼성</td>
								<td>LG</td>
								<td>대구</td>
								<td>21,817</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/13</td>
								<td>토</td>
								<td>KT</td>
								<td>롯데</td>
								<td>수원</td>
								<td>18,700</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/13</td>
								<td>토</td>
								<td>키움</td>
								<td>NC</td>
								<td>고척</td>
								<td>6,573</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/14</td>
								<td>일</td>
								<td>SSG</td>
								<td>한화</td>
								<td>문학</td>
								<td>20,757</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/14</td>
								<td>일</td>
								<td>두산</td>
								<td>KIA</td>
								<td>잠실</td>
								<td>23,750</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/14</td>
								<td>일</td>
								<td>삼성</td>
								<td>LG</td>
								<td>대구</td>
								<td>18,569</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/14</td>
								<td>일</td>
								<td>KT</td>
								<td>롯데</td>
								<td>수원</td>
								<td>15,470</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/14</td>
								<td>일</td>
								<td>키움</td>
								<td>NC</td>
								<td>고척</td>
								<td>5,634</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/16</td>
								<td>화</td>
								<td>삼성</td>
								<td>KIA</td>
								<td>대구</td>
								<td>9,112</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/16</td>
								<td>화</td>
								<td>LG</td>
								<td>KT</td>
								<td>잠실</td>
								<td>8,567</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/16</td>
								<td>화</td>
								<td>한화</td>
								<td>롯데</td>
								<td>대전</td>
								<td>6,138</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/16</td>
								<td>화</td>
								<td>키움</td>
								<td>두산</td>
								<td>고척</td>
								<td>5,662</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/16</td>
								<td>화</td>
								<td>NC</td>
								<td>SSG</td>
								<td>창원</td>
								<td>4,113</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/17</td>
								<td>수</td>
								<td>삼성</td>
								<td>KIA</td>
								<td>대구</td>
								<td>10,979</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/17</td>
								<td>수</td>
								<td>LG</td>
								<td>KT</td>
								<td>잠실</td>
								<td>9,838</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/17</td>
								<td>수</td>
								<td>한화</td>
								<td>롯데</td>
								<td>대전</td>
								<td>6,269</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/17</td>
								<td>수</td>
								<td>키움</td>
								<td>두산</td>
								<td>고척</td>
								<td>5,232</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/17</td>
								<td>수</td>
								<td>NC</td>
								<td>SSG</td>
								<td>창원</td>
								<td>4,344</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/18</td>
								<td>목</td>
								<td>LG</td>
								<td>KT</td>
								<td>잠실</td>
								<td>9,155</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/18</td>
								<td>목</td>
								<td>한화</td>
								<td>롯데</td>
								<td>대전</td>
								<td>6,116</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/18</td>
								<td>목</td>
								<td>키움</td>
								<td>두산</td>
								<td>고척</td>
								<td>5,742</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/19</td>
								<td>금</td>
								<td>LG</td>
								<td>한화</td>
								<td>잠실</td>
								<td>19,798</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/19</td>
								<td>금</td>
								<td>KT</td>
								<td>두산</td>
								<td>수원</td>
								<td>6,817</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/19</td>
								<td>금</td>
								<td>롯데</td>
								<td>SSG</td>
								<td>사직</td>
								<td>19,011</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/19</td>
								<td>금</td>
								<td>NC</td>
								<td>삼성</td>
								<td>창원</td>
								<td>8,493</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/19</td>
								<td>금</td>
								<td>KIA</td>
								<td>키움</td>
								<td>광주</td>
								<td>11,290</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/20</td>
								<td>토</td>
								<td>LG</td>
								<td>한화</td>
								<td>잠실</td>
								<td>23,750</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/20</td>
								<td>토</td>
								<td>KT</td>
								<td>두산</td>
								<td>수원</td>
								<td>13,253</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/20</td>
								<td>토</td>
								<td>롯데</td>
								<td>SSG</td>
								<td>사직</td>
								<td>22,990</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/20</td>
								<td>토</td>
								<td>NC</td>
								<td>삼성</td>
								<td>창원</td>
								<td>14,870</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/20</td>
								<td>토</td>
								<td>KIA</td>
								<td>키움</td>
								<td>광주</td>
								<td>19,030</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/21</td>
								<td>일</td>
								<td>LG</td>
								<td>한화</td>
								<td>잠실</td>
								<td>22,054</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/21</td>
								<td>일</td>
								<td>KT</td>
								<td>두산</td>
								<td>수원</td>
								<td>10,521</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/21</td>
								<td>일</td>
								<td>롯데</td>
								<td>SSG</td>
								<td>사직</td>
								<td>22,990</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/21</td>
								<td>일</td>
								<td>NC</td>
								<td>삼성</td>
								<td>창원</td>
								<td>10,910</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/21</td>
								<td>일</td>
								<td>KIA</td>
								<td>키움</td>
								<td>광주</td>
								<td>14,617</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/23</td>
								<td>화</td>
								<td>한화</td>
								<td>KIA</td>
								<td>대전</td>
								<td>6,376</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/23</td>
								<td>화</td>
								<td>SSG</td>
								<td>LG</td>
								<td>문학</td>
								<td>12,508</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/23</td>
								<td>화</td>
								<td>롯데</td>
								<td>NC</td>
								<td>사직</td>
								<td>15,047</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/23</td>
								<td>화</td>
								<td>두산</td>
								<td>삼성</td>
								<td>잠실</td>
								<td>10,733</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/23</td>
								<td>화</td>
								<td>KT</td>
								<td>키움</td>
								<td>수원</td>
								<td>4,203</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/24</td>
								<td>수</td>
								<td>한화</td>
								<td>KIA</td>
								<td>대전</td>
								<td>7,004</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/24</td>
								<td>수</td>
								<td>SSG</td>
								<td>LG</td>
								<td>문학</td>
								<td>16,829</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/24</td>
								<td>수</td>
								<td>롯데</td>
								<td>NC</td>
								<td>사직</td>
								<td>14,244</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/24</td>
								<td>수</td>
								<td>두산</td>
								<td>삼성</td>
								<td>잠실</td>
								<td>11,108</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/24</td>
								<td>수</td>
								<td>KT</td>
								<td>키움</td>
								<td>수원</td>
								<td>5,173</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/25</td>
								<td>목</td>
								<td>한화</td>
								<td>KIA</td>
								<td>대전</td>
								<td>8,186</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/25</td>
								<td>목</td>
								<td>SSG</td>
								<td>LG</td>
								<td>문학</td>
								<td>17,575</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/25</td>
								<td>목</td>
								<td>롯데</td>
								<td>NC</td>
								<td>사직</td>
								<td>15,221</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/25</td>
								<td>목</td>
								<td>두산</td>
								<td>삼성</td>
								<td>잠실</td>
								<td>11,005</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/25</td>
								<td>목</td>
								<td>KT</td>
								<td>키움</td>
								<td>수원</td>
								<td>5,235</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/26</td>
								<td>금</td>
								<td>NC</td>
								<td>한화</td>
								<td>창원</td>
								<td>5,952</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/26</td>
								<td>금</td>
								<td>삼성</td>
								<td>KT</td>
								<td>대구</td>
								<td>12,874</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/26</td>
								<td>금</td>
								<td>KIA</td>
								<td>LG</td>
								<td>광주</td>
								<td>10,954</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/26</td>
								<td>금</td>
								<td>키움</td>
								<td>롯데</td>
								<td>고척</td>
								<td>11,692</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/26</td>
								<td>금</td>
								<td>두산</td>
								<td>SSG</td>
								<td>잠실</td>
								<td>10,428</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/27</td>
								<td>토</td>
								<td>NC</td>
								<td>한화</td>
								<td>창원</td>
								<td>9,558</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/27</td>
								<td>토</td>
								<td>삼성</td>
								<td>KT</td>
								<td>대구</td>
								<td>17,305</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/27</td>
								<td>토</td>
								<td>KIA</td>
								<td>LG</td>
								<td>광주</td>
								<td>17,931</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/27</td>
								<td>토</td>
								<td>키움</td>
								<td>롯데</td>
								<td>고척</td>
								<td>16,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/28</td>
								<td>일</td>
								<td>삼성</td>
								<td>KT</td>
								<td>대구</td>
								<td>14,523</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/28</td>
								<td>일</td>
								<td>KIA</td>
								<td>LG</td>
								<td>광주</td>
								<td>17,015</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/28</td>
								<td>일</td>
								<td>키움</td>
								<td>롯데</td>
								<td>고척</td>
								<td>16,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/30</td>
								<td>화</td>
								<td>KIA</td>
								<td>KT</td>
								<td>광주</td>
								<td>5,352</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/30</td>
								<td>화</td>
								<td>LG</td>
								<td>롯데</td>
								<td>잠실</td>
								<td>20,330</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/30</td>
								<td>화</td>
								<td>NC</td>
								<td>두산</td>
								<td>창원</td>
								<td>3,180</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/30</td>
								<td>화</td>
								<td>SSG</td>
								<td>삼성</td>
								<td>문학</td>
								<td>10,232</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/30</td>
								<td>화</td>
								<td>한화</td>
								<td>키움</td>
								<td>대전</td>
								<td>4,486</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/31</td>
								<td>수</td>
								<td>KIA</td>
								<td>KT</td>
								<td>광주</td>
								<td>7,244</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/31</td>
								<td>수</td>
								<td>LG</td>
								<td>롯데</td>
								<td>잠실</td>
								<td>21,269</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/31</td>
								<td>수</td>
								<td>NC</td>
								<td>두산</td>
								<td>창원</td>
								<td>4,180</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/31</td>
								<td>수</td>
								<td>SSG</td>
								<td>삼성</td>
								<td>문학</td>
								<td>10,745</td>
							</tr>
						
							<tr class="order">
								<td>2023/05/31</td>
								<td>수</td>
								<td>한화</td>
								<td>키움</td>
								<td>대전</td>
								<td>4,384</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/01</td>
								<td>목</td>
								<td>LG</td>
								<td>롯데</td>
								<td>잠실</td>
								<td>22,020</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/01</td>
								<td>목</td>
								<td>SSG</td>
								<td>삼성</td>
								<td>문학</td>
								<td>9,028</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/01</td>
								<td>목</td>
								<td>한화</td>
								<td>키움</td>
								<td>대전</td>
								<td>5,040</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/02</td>
								<td>금</td>
								<td>롯데</td>
								<td>KIA</td>
								<td>사직</td>
								<td>18,996</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/02</td>
								<td>금</td>
								<td>LG</td>
								<td>NC</td>
								<td>잠실</td>
								<td>10,238</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/02</td>
								<td>금</td>
								<td>KT</td>
								<td>두산</td>
								<td>수원</td>
								<td>5,157</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/02</td>
								<td>금</td>
								<td>한화</td>
								<td>삼성</td>
								<td>대전</td>
								<td>6,675</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/02</td>
								<td>금</td>
								<td>SSG</td>
								<td>키움</td>
								<td>문학</td>
								<td>12,533</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/03</td>
								<td>토</td>
								<td>롯데</td>
								<td>KIA</td>
								<td>사직</td>
								<td>22,990</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/03</td>
								<td>토</td>
								<td>LG</td>
								<td>NC</td>
								<td>잠실</td>
								<td>18,890</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/03</td>
								<td>토</td>
								<td>KT</td>
								<td>두산</td>
								<td>수원</td>
								<td>12,155</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/03</td>
								<td>토</td>
								<td>한화</td>
								<td>삼성</td>
								<td>대전</td>
								<td>12,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/03</td>
								<td>토</td>
								<td>SSG</td>
								<td>키움</td>
								<td>문학</td>
								<td>19,071</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/04</td>
								<td>일</td>
								<td>롯데</td>
								<td>KIA</td>
								<td>사직</td>
								<td>22,990</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/04</td>
								<td>일</td>
								<td>LG</td>
								<td>NC</td>
								<td>잠실</td>
								<td>15,096</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/04</td>
								<td>일</td>
								<td>KT</td>
								<td>두산</td>
								<td>수원</td>
								<td>10,239</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/04</td>
								<td>일</td>
								<td>한화</td>
								<td>삼성</td>
								<td>대전</td>
								<td>12,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/04</td>
								<td>일</td>
								<td>SSG</td>
								<td>키움</td>
								<td>문학</td>
								<td>17,007</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/06</td>
								<td>화</td>
								<td>두산</td>
								<td>한화</td>
								<td>잠실</td>
								<td>21,146</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/06</td>
								<td>화</td>
								<td>롯데</td>
								<td>KT</td>
								<td>사직</td>
								<td>20,441</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/06</td>
								<td>화</td>
								<td>키움</td>
								<td>LG</td>
								<td>고척</td>
								<td>14,903</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/06</td>
								<td>화</td>
								<td>삼성</td>
								<td>NC</td>
								<td>대구</td>
								<td>14,639</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/06</td>
								<td>화</td>
								<td>KIA</td>
								<td>SSG</td>
								<td>광주</td>
								<td>15,130</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/07</td>
								<td>수</td>
								<td>두산</td>
								<td>한화</td>
								<td>잠실</td>
								<td>8,497</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/07</td>
								<td>수</td>
								<td>롯데</td>
								<td>KT</td>
								<td>사직</td>
								<td>10,066</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/07</td>
								<td>수</td>
								<td>키움</td>
								<td>LG</td>
								<td>고척</td>
								<td>5,390</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/07</td>
								<td>수</td>
								<td>삼성</td>
								<td>NC</td>
								<td>대구</td>
								<td>7,119</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/07</td>
								<td>수</td>
								<td>KIA</td>
								<td>SSG</td>
								<td>광주</td>
								<td>7,569</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/08</td>
								<td>목</td>
								<td>두산</td>
								<td>한화</td>
								<td>잠실</td>
								<td>8,509</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/08</td>
								<td>목</td>
								<td>롯데</td>
								<td>KT</td>
								<td>사직</td>
								<td>10,504</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/08</td>
								<td>목</td>
								<td>키움</td>
								<td>LG</td>
								<td>고척</td>
								<td>6,076</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/08</td>
								<td>목</td>
								<td>삼성</td>
								<td>NC</td>
								<td>대구</td>
								<td>5,989</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/08</td>
								<td>목</td>
								<td>KIA</td>
								<td>SSG</td>
								<td>광주</td>
								<td>6,646</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/09</td>
								<td>금</td>
								<td>두산</td>
								<td>KIA</td>
								<td>잠실</td>
								<td>16,250</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/09</td>
								<td>금</td>
								<td>한화</td>
								<td>LG</td>
								<td>대전</td>
								<td>6,005</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/09</td>
								<td>금</td>
								<td>삼성</td>
								<td>롯데</td>
								<td>대구</td>
								<td>15,893</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/09</td>
								<td>금</td>
								<td>NC</td>
								<td>SSG</td>
								<td>창원</td>
								<td>5,110</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/09</td>
								<td>금</td>
								<td>KT</td>
								<td>키움</td>
								<td>수원</td>
								<td>5,033</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/10</td>
								<td>토</td>
								<td>두산</td>
								<td>KIA</td>
								<td>잠실</td>
								<td>22,233</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/10</td>
								<td>토</td>
								<td>한화</td>
								<td>LG</td>
								<td>대전</td>
								<td>11,072</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/10</td>
								<td>토</td>
								<td>삼성</td>
								<td>롯데</td>
								<td>대구</td>
								<td>24,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/10</td>
								<td>토</td>
								<td>NC</td>
								<td>SSG</td>
								<td>창원</td>
								<td>11,026</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/10</td>
								<td>토</td>
								<td>KT</td>
								<td>키움</td>
								<td>수원</td>
								<td>9,622</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/11</td>
								<td>일</td>
								<td>두산</td>
								<td>KIA</td>
								<td>잠실</td>
								<td>18,623</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/11</td>
								<td>일</td>
								<td>한화</td>
								<td>LG</td>
								<td>대전</td>
								<td>7,601</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/11</td>
								<td>일</td>
								<td>삼성</td>
								<td>롯데</td>
								<td>대구</td>
								<td>18,496</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/11</td>
								<td>일</td>
								<td>NC</td>
								<td>SSG</td>
								<td>창원</td>
								<td>7,210</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/11</td>
								<td>일</td>
								<td>KT</td>
								<td>키움</td>
								<td>수원</td>
								<td>6,806</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/13</td>
								<td>화</td>
								<td>롯데</td>
								<td>한화</td>
								<td>사직</td>
								<td>16,007</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/13</td>
								<td>화</td>
								<td>키움</td>
								<td>KIA</td>
								<td>고척</td>
								<td>7,834</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/13</td>
								<td>화</td>
								<td>SSG</td>
								<td>KT</td>
								<td>문학</td>
								<td>6,568</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/13</td>
								<td>화</td>
								<td>NC</td>
								<td>두산</td>
								<td>창원</td>
								<td>3,699</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/13</td>
								<td>화</td>
								<td>LG</td>
								<td>삼성</td>
								<td>잠실</td>
								<td>11,103</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/14</td>
								<td>수</td>
								<td>롯데</td>
								<td>한화</td>
								<td>사직</td>
								<td>10,803</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/14</td>
								<td>수</td>
								<td>키움</td>
								<td>KIA</td>
								<td>고척</td>
								<td>8,016</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/14</td>
								<td>수</td>
								<td>SSG</td>
								<td>KT</td>
								<td>문학</td>
								<td>6,579</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/14</td>
								<td>수</td>
								<td>NC</td>
								<td>두산</td>
								<td>창원</td>
								<td>3,154</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/14</td>
								<td>수</td>
								<td>LG</td>
								<td>삼성</td>
								<td>잠실</td>
								<td>11,725</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/15</td>
								<td>목</td>
								<td>롯데</td>
								<td>한화</td>
								<td>사직</td>
								<td>12,594</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/15</td>
								<td>목</td>
								<td>키움</td>
								<td>KIA</td>
								<td>고척</td>
								<td>8,528</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/15</td>
								<td>목</td>
								<td>SSG</td>
								<td>KT</td>
								<td>문학</td>
								<td>6,736</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/15</td>
								<td>목</td>
								<td>NC</td>
								<td>두산</td>
								<td>창원</td>
								<td>3,633</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/15</td>
								<td>목</td>
								<td>LG</td>
								<td>삼성</td>
								<td>잠실</td>
								<td>12,023</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/16</td>
								<td>금</td>
								<td>SSG</td>
								<td>롯데</td>
								<td>문학</td>
								<td>18,013</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/16</td>
								<td>금</td>
								<td>KIA</td>
								<td>NC</td>
								<td>광주</td>
								<td>10,170</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/16</td>
								<td>금</td>
								<td>LG</td>
								<td>두산</td>
								<td>잠실</td>
								<td>18,826</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/16</td>
								<td>금</td>
								<td>KT</td>
								<td>삼성</td>
								<td>수원</td>
								<td>6,998</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/16</td>
								<td>금</td>
								<td>한화</td>
								<td>키움</td>
								<td>대전</td>
								<td>7,005</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/17</td>
								<td>토</td>
								<td>SSG</td>
								<td>롯데</td>
								<td>문학</td>
								<td>23,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/17</td>
								<td>토</td>
								<td>KIA</td>
								<td>NC</td>
								<td>광주</td>
								<td>15,992</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/17</td>
								<td>토</td>
								<td>LG</td>
								<td>두산</td>
								<td>잠실</td>
								<td>22,878</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/17</td>
								<td>토</td>
								<td>KT</td>
								<td>삼성</td>
								<td>수원</td>
								<td>14,935</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/17</td>
								<td>토</td>
								<td>한화</td>
								<td>키움</td>
								<td>대전</td>
								<td>11,008</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/18</td>
								<td>일</td>
								<td>SSG</td>
								<td>롯데</td>
								<td>문학</td>
								<td>19,156</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/18</td>
								<td>일</td>
								<td>KIA</td>
								<td>NC</td>
								<td>광주</td>
								<td>13,967</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/18</td>
								<td>일</td>
								<td>LG</td>
								<td>두산</td>
								<td>잠실</td>
								<td>19,038</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/18</td>
								<td>일</td>
								<td>KT</td>
								<td>삼성</td>
								<td>수원</td>
								<td>10,137</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/18</td>
								<td>일</td>
								<td>한화</td>
								<td>키움</td>
								<td>대전</td>
								<td>8,163</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/20</td>
								<td>화</td>
								<td>한화</td>
								<td>KIA</td>
								<td>대전</td>
								<td>5,451</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/20</td>
								<td>화</td>
								<td>NC</td>
								<td>LG</td>
								<td>창원</td>
								<td>3,433</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/20</td>
								<td>화</td>
								<td>KT</td>
								<td>롯데</td>
								<td>수원</td>
								<td>5,773</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/20</td>
								<td>화</td>
								<td>두산</td>
								<td>SSG</td>
								<td>잠실</td>
								<td>6,186</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/20</td>
								<td>화</td>
								<td>삼성</td>
								<td>키움</td>
								<td>대구</td>
								<td>7,667</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/21</td>
								<td>수</td>
								<td>한화</td>
								<td>KIA</td>
								<td>대전</td>
								<td>5,207</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/21</td>
								<td>수</td>
								<td>NC</td>
								<td>LG</td>
								<td>창원</td>
								<td>3,571</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/21</td>
								<td>수</td>
								<td>KT</td>
								<td>롯데</td>
								<td>수원</td>
								<td>6,024</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/21</td>
								<td>수</td>
								<td>두산</td>
								<td>SSG</td>
								<td>잠실</td>
								<td>5,473</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/21</td>
								<td>수</td>
								<td>삼성</td>
								<td>키움</td>
								<td>대구</td>
								<td>7,453</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/22</td>
								<td>목</td>
								<td>한화</td>
								<td>KIA</td>
								<td>대전</td>
								<td>7,675</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/22</td>
								<td>목</td>
								<td>NC</td>
								<td>LG</td>
								<td>창원</td>
								<td>4,997</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/22</td>
								<td>목</td>
								<td>KT</td>
								<td>롯데</td>
								<td>수원</td>
								<td>7,861</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/22</td>
								<td>목</td>
								<td>두산</td>
								<td>SSG</td>
								<td>잠실</td>
								<td>7,291</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/22</td>
								<td>목</td>
								<td>삼성</td>
								<td>키움</td>
								<td>대구</td>
								<td>10,176</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/23</td>
								<td>금</td>
								<td>NC</td>
								<td>한화</td>
								<td>창원</td>
								<td>6,376</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/23</td>
								<td>금</td>
								<td>KIA</td>
								<td>KT</td>
								<td>광주</td>
								<td>9,018</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/23</td>
								<td>금</td>
								<td>LG</td>
								<td>롯데</td>
								<td>잠실</td>
								<td>21,089</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/23</td>
								<td>금</td>
								<td>키움</td>
								<td>두산</td>
								<td>고척</td>
								<td>7,316</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/23</td>
								<td>금</td>
								<td>SSG</td>
								<td>삼성</td>
								<td>문학</td>
								<td>12,744</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/24</td>
								<td>토</td>
								<td>NC</td>
								<td>한화</td>
								<td>창원</td>
								<td>13,791</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/24</td>
								<td>토</td>
								<td>KIA</td>
								<td>KT</td>
								<td>광주</td>
								<td>14,043</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/24</td>
								<td>토</td>
								<td>LG</td>
								<td>롯데</td>
								<td>잠실</td>
								<td>23,750</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/24</td>
								<td>토</td>
								<td>키움</td>
								<td>두산</td>
								<td>고척</td>
								<td>11,717</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/24</td>
								<td>토</td>
								<td>SSG</td>
								<td>삼성</td>
								<td>문학</td>
								<td>20,062</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/25</td>
								<td>일</td>
								<td>LG</td>
								<td>롯데</td>
								<td>잠실</td>
								<td>20,846</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/25</td>
								<td>일</td>
								<td>키움</td>
								<td>두산</td>
								<td>고척</td>
								<td>9,549</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/25</td>
								<td>일</td>
								<td>SSG</td>
								<td>삼성</td>
								<td>문학</td>
								<td>14,722</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/27</td>
								<td>화</td>
								<td>한화</td>
								<td>KT</td>
								<td>대전</td>
								<td>4,625</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/27</td>
								<td>화</td>
								<td>SSG</td>
								<td>LG</td>
								<td>문학</td>
								<td>12,244</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/27</td>
								<td>화</td>
								<td>두산</td>
								<td>NC</td>
								<td>잠실</td>
								<td>5,302</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/27</td>
								<td>화</td>
								<td>롯데</td>
								<td>삼성</td>
								<td>사직</td>
								<td>11,654</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/27</td>
								<td>화</td>
								<td>KIA</td>
								<td>키움</td>
								<td>광주</td>
								<td>5,349</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/28</td>
								<td>수</td>
								<td>한화</td>
								<td>KT</td>
								<td>대전</td>
								<td>5,007</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/28</td>
								<td>수</td>
								<td>SSG</td>
								<td>LG</td>
								<td>문학</td>
								<td>11,045</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/28</td>
								<td>수</td>
								<td>두산</td>
								<td>NC</td>
								<td>잠실</td>
								<td>5,400</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/28</td>
								<td>수</td>
								<td>롯데</td>
								<td>삼성</td>
								<td>사직</td>
								<td>13,787</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/28</td>
								<td>수</td>
								<td>KIA</td>
								<td>키움</td>
								<td>광주</td>
								<td>4,816</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/30</td>
								<td>금</td>
								<td>삼성</td>
								<td>한화</td>
								<td>대구</td>
								<td>8,114</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/30</td>
								<td>금</td>
								<td>LG</td>
								<td>KIA</td>
								<td>잠실</td>
								<td>20,568</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/30</td>
								<td>금</td>
								<td>KT</td>
								<td>NC</td>
								<td>수원</td>
								<td>4,596</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/30</td>
								<td>금</td>
								<td>롯데</td>
								<td>두산</td>
								<td>울산</td>
								<td>6,894</td>
							</tr>
						
							<tr class="order">
								<td>2023/06/30</td>
								<td>금</td>
								<td>키움</td>
								<td>SSG</td>
								<td>고척</td>
								<td>7,164</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/01</td>
								<td>토</td>
								<td>삼성</td>
								<td>한화</td>
								<td>대구</td>
								<td>18,151</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/01</td>
								<td>토</td>
								<td>LG</td>
								<td>KIA</td>
								<td>잠실</td>
								<td>23,750</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/01</td>
								<td>토</td>
								<td>KT</td>
								<td>NC</td>
								<td>수원</td>
								<td>9,551</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/01</td>
								<td>토</td>
								<td>롯데</td>
								<td>두산</td>
								<td>울산</td>
								<td>10,013</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/01</td>
								<td>토</td>
								<td>키움</td>
								<td>SSG</td>
								<td>고척</td>
								<td>10,836</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/02</td>
								<td>일</td>
								<td>삼성</td>
								<td>한화</td>
								<td>대구</td>
								<td>12,395</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/02</td>
								<td>일</td>
								<td>LG</td>
								<td>KIA</td>
								<td>잠실</td>
								<td>20,959</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/02</td>
								<td>일</td>
								<td>KT</td>
								<td>NC</td>
								<td>수원</td>
								<td>5,406</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/02</td>
								<td>일</td>
								<td>롯데</td>
								<td>두산</td>
								<td>울산</td>
								<td>7,588</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/02</td>
								<td>일</td>
								<td>키움</td>
								<td>SSG</td>
								<td>고척</td>
								<td>9,512</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/04</td>
								<td>화</td>
								<td>키움</td>
								<td>NC</td>
								<td>고척</td>
								<td>4,474</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/04</td>
								<td>화</td>
								<td>삼성</td>
								<td>두산</td>
								<td>포항</td>
								<td>4,182</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/05</td>
								<td>수</td>
								<td>SSG</td>
								<td>KIA</td>
								<td>문학</td>
								<td>13,025</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/05</td>
								<td>수</td>
								<td>LG</td>
								<td>KT</td>
								<td>잠실</td>
								<td>9,707</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/05</td>
								<td>수</td>
								<td>한화</td>
								<td>롯데</td>
								<td>대전</td>
								<td>7,760</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/05</td>
								<td>수</td>
								<td>키움</td>
								<td>NC</td>
								<td>고척</td>
								<td>4,027</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/05</td>
								<td>수</td>
								<td>삼성</td>
								<td>두산</td>
								<td>포항</td>
								<td>5,902</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/06</td>
								<td>목</td>
								<td>SSG</td>
								<td>KIA</td>
								<td>문학</td>
								<td>17,513</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/06</td>
								<td>목</td>
								<td>LG</td>
								<td>KT</td>
								<td>잠실</td>
								<td>10,736</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/06</td>
								<td>목</td>
								<td>한화</td>
								<td>롯데</td>
								<td>대전</td>
								<td>10,061</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/06</td>
								<td>목</td>
								<td>키움</td>
								<td>NC</td>
								<td>고척</td>
								<td>4,013</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/06</td>
								<td>목</td>
								<td>삼성</td>
								<td>두산</td>
								<td>포항</td>
								<td>6,923</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/07</td>
								<td>금</td>
								<td>KT</td>
								<td>KIA</td>
								<td>수원</td>
								<td>16,315</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/07</td>
								<td>금</td>
								<td>두산</td>
								<td>키움</td>
								<td>잠실</td>
								<td>14,123</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/08</td>
								<td>토</td>
								<td>KT</td>
								<td>KIA</td>
								<td>수원</td>
								<td>18,700</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/08</td>
								<td>토</td>
								<td>롯데</td>
								<td>LG</td>
								<td>사직</td>
								<td>19,496</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/08</td>
								<td>토</td>
								<td>한화</td>
								<td>SSG</td>
								<td>대전</td>
								<td>12,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/08</td>
								<td>토</td>
								<td>NC</td>
								<td>삼성</td>
								<td>창원</td>
								<td>12,462</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/08</td>
								<td>토</td>
								<td>두산</td>
								<td>키움</td>
								<td>잠실</td>
								<td>19,676</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/09</td>
								<td>일</td>
								<td>KT</td>
								<td>KIA</td>
								<td>수원</td>
								<td>18,700</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/09</td>
								<td>일</td>
								<td>롯데</td>
								<td>LG</td>
								<td>사직</td>
								<td>15,860</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/09</td>
								<td>일</td>
								<td>한화</td>
								<td>SSG</td>
								<td>대전</td>
								<td>10,168</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/09</td>
								<td>일</td>
								<td>NC</td>
								<td>삼성</td>
								<td>창원</td>
								<td>8,522</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/09</td>
								<td>일</td>
								<td>두산</td>
								<td>키움</td>
								<td>잠실</td>
								<td>11,472</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/11</td>
								<td>화</td>
								<td>키움</td>
								<td>KT</td>
								<td>고척</td>
								<td>4,217</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/12</td>
								<td>수</td>
								<td>LG</td>
								<td>한화</td>
								<td>잠실</td>
								<td>17,812</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/12</td>
								<td>수</td>
								<td>키움</td>
								<td>KT</td>
								<td>고척</td>
								<td>3,890</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/12</td>
								<td>수</td>
								<td>NC</td>
								<td>롯데</td>
								<td>창원</td>
								<td>13,074</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/12</td>
								<td>수</td>
								<td>SSG</td>
								<td>두산</td>
								<td>문학</td>
								<td>19,699</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/12</td>
								<td>수</td>
								<td>KIA</td>
								<td>삼성</td>
								<td>광주</td>
								<td>8,470</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/13</td>
								<td>목</td>
								<td>키움</td>
								<td>KT</td>
								<td>고척</td>
								<td>4,520</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/13</td>
								<td>목</td>
								<td>NC</td>
								<td>롯데</td>
								<td>창원</td>
								<td>10,316</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/13</td>
								<td>목</td>
								<td>KIA</td>
								<td>삼성</td>
								<td>광주</td>
								<td>7,085</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/21</td>
								<td>금</td>
								<td>삼성</td>
								<td>KT</td>
								<td>대구</td>
								<td>7,833</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/21</td>
								<td>금</td>
								<td>한화</td>
								<td>NC</td>
								<td>대전</td>
								<td>8,475</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/21</td>
								<td>금</td>
								<td>KIA</td>
								<td>두산</td>
								<td>광주</td>
								<td>9,779</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/21</td>
								<td>금</td>
								<td>LG</td>
								<td>SSG</td>
								<td>잠실</td>
								<td>17,524</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/21</td>
								<td>금</td>
								<td>롯데</td>
								<td>키움</td>
								<td>사직</td>
								<td>13,431</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/22</td>
								<td>토</td>
								<td>삼성</td>
								<td>KT</td>
								<td>대구</td>
								<td>10,356</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/22</td>
								<td>토</td>
								<td>한화</td>
								<td>NC</td>
								<td>대전</td>
								<td>10,021</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/22</td>
								<td>토</td>
								<td>롯데</td>
								<td>키움</td>
								<td>사직</td>
								<td>14,266</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/23</td>
								<td>일</td>
								<td>삼성</td>
								<td>KT</td>
								<td>대구</td>
								<td>8,613</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/23</td>
								<td>일</td>
								<td>롯데</td>
								<td>키움</td>
								<td>사직</td>
								<td>11,470</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/25</td>
								<td>화</td>
								<td>키움</td>
								<td>한화</td>
								<td>고척</td>
								<td>9,886</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/25</td>
								<td>화</td>
								<td>NC</td>
								<td>KIA</td>
								<td>창원</td>
								<td>5,668</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/25</td>
								<td>화</td>
								<td>KT</td>
								<td>LG</td>
								<td>수원</td>
								<td>7,948</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/25</td>
								<td>화</td>
								<td>두산</td>
								<td>롯데</td>
								<td>잠실</td>
								<td>12,700</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/25</td>
								<td>화</td>
								<td>삼성</td>
								<td>SSG</td>
								<td>대구</td>
								<td>5,557</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/26</td>
								<td>수</td>
								<td>키움</td>
								<td>한화</td>
								<td>고척</td>
								<td>11,324</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/26</td>
								<td>수</td>
								<td>NC</td>
								<td>KIA</td>
								<td>창원</td>
								<td>6,325</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/26</td>
								<td>수</td>
								<td>KT</td>
								<td>LG</td>
								<td>수원</td>
								<td>8,134</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/26</td>
								<td>수</td>
								<td>두산</td>
								<td>롯데</td>
								<td>잠실</td>
								<td>13,620</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/26</td>
								<td>수</td>
								<td>삼성</td>
								<td>SSG</td>
								<td>대구</td>
								<td>6,955</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/27</td>
								<td>목</td>
								<td>키움</td>
								<td>한화</td>
								<td>고척</td>
								<td>11,650</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/27</td>
								<td>목</td>
								<td>NC</td>
								<td>KIA</td>
								<td>창원</td>
								<td>7,279</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/27</td>
								<td>목</td>
								<td>KT</td>
								<td>LG</td>
								<td>수원</td>
								<td>8,413</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/27</td>
								<td>목</td>
								<td>두산</td>
								<td>롯데</td>
								<td>잠실</td>
								<td>12,511</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/27</td>
								<td>목</td>
								<td>삼성</td>
								<td>SSG</td>
								<td>대구</td>
								<td>7,663</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/28</td>
								<td>금</td>
								<td>SSG</td>
								<td>한화</td>
								<td>문학</td>
								<td>14,386</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/28</td>
								<td>금</td>
								<td>NC</td>
								<td>KT</td>
								<td>창원</td>
								<td>4,676</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/28</td>
								<td>금</td>
								<td>두산</td>
								<td>LG</td>
								<td>잠실</td>
								<td>16,987</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/28</td>
								<td>금</td>
								<td>KIA</td>
								<td>롯데</td>
								<td>광주</td>
								<td>10,295</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/28</td>
								<td>금</td>
								<td>키움</td>
								<td>삼성</td>
								<td>고척</td>
								<td>7,755</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/29</td>
								<td>토</td>
								<td>SSG</td>
								<td>한화</td>
								<td>문학</td>
								<td>21,344</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/29</td>
								<td>토</td>
								<td>NC</td>
								<td>KT</td>
								<td>창원</td>
								<td>8,309</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/29</td>
								<td>토</td>
								<td>두산</td>
								<td>LG</td>
								<td>잠실</td>
								<td>21,126</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/29</td>
								<td>토</td>
								<td>KIA</td>
								<td>롯데</td>
								<td>광주</td>
								<td>14,754</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/29</td>
								<td>토</td>
								<td>키움</td>
								<td>삼성</td>
								<td>고척</td>
								<td>11,851</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/30</td>
								<td>일</td>
								<td>SSG</td>
								<td>한화</td>
								<td>문학</td>
								<td>18,158</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/30</td>
								<td>일</td>
								<td>NC</td>
								<td>KT</td>
								<td>창원</td>
								<td>6,181</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/30</td>
								<td>일</td>
								<td>두산</td>
								<td>LG</td>
								<td>잠실</td>
								<td>19,500</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/30</td>
								<td>일</td>
								<td>KIA</td>
								<td>롯데</td>
								<td>광주</td>
								<td>11,796</td>
							</tr>
						
							<tr class="order">
								<td>2023/07/30</td>
								<td>일</td>
								<td>키움</td>
								<td>삼성</td>
								<td>고척</td>
								<td>11,235</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/01</td>
								<td>화</td>
								<td>삼성</td>
								<td>KIA</td>
								<td>포항</td>
								<td>6,912</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/01</td>
								<td>화</td>
								<td>롯데</td>
								<td>NC</td>
								<td>사직</td>
								<td>13,326</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/01</td>
								<td>화</td>
								<td>한화</td>
								<td>두산</td>
								<td>대전</td>
								<td>10,225</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/01</td>
								<td>화</td>
								<td>KT</td>
								<td>SSG</td>
								<td>수원</td>
								<td>7,831</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/01</td>
								<td>화</td>
								<td>LG</td>
								<td>키움</td>
								<td>잠실</td>
								<td>12,159</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/02</td>
								<td>수</td>
								<td>삼성</td>
								<td>KIA</td>
								<td>포항</td>
								<td>6,477</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/02</td>
								<td>수</td>
								<td>롯데</td>
								<td>NC</td>
								<td>사직</td>
								<td>11,444</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/02</td>
								<td>수</td>
								<td>한화</td>
								<td>두산</td>
								<td>대전</td>
								<td>9,011</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/02</td>
								<td>수</td>
								<td>KT</td>
								<td>SSG</td>
								<td>수원</td>
								<td>7,780</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/02</td>
								<td>수</td>
								<td>LG</td>
								<td>키움</td>
								<td>잠실</td>
								<td>11,740</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/03</td>
								<td>목</td>
								<td>삼성</td>
								<td>KIA</td>
								<td>포항</td>
								<td>6,357</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/03</td>
								<td>목</td>
								<td>롯데</td>
								<td>NC</td>
								<td>사직</td>
								<td>10,162</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/03</td>
								<td>목</td>
								<td>한화</td>
								<td>두산</td>
								<td>대전</td>
								<td>9,024</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/03</td>
								<td>목</td>
								<td>KT</td>
								<td>SSG</td>
								<td>수원</td>
								<td>7,521</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/03</td>
								<td>목</td>
								<td>LG</td>
								<td>키움</td>
								<td>잠실</td>
								<td>12,179</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/04</td>
								<td>금</td>
								<td>KIA</td>
								<td>한화</td>
								<td>광주</td>
								<td>11,495</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/04</td>
								<td>금</td>
								<td>두산</td>
								<td>KT</td>
								<td>잠실</td>
								<td>6,358</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/04</td>
								<td>금</td>
								<td>삼성</td>
								<td>LG</td>
								<td>대구</td>
								<td>10,856</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/04</td>
								<td>금</td>
								<td>롯데</td>
								<td>SSG</td>
								<td>사직</td>
								<td>8,545</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/04</td>
								<td>금</td>
								<td>NC</td>
								<td>키움</td>
								<td>창원</td>
								<td>5,107</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/05</td>
								<td>토</td>
								<td>KIA</td>
								<td>한화</td>
								<td>광주</td>
								<td>13,487</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/05</td>
								<td>토</td>
								<td>두산</td>
								<td>KT</td>
								<td>잠실</td>
								<td>8,847</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/05</td>
								<td>토</td>
								<td>삼성</td>
								<td>LG</td>
								<td>대구</td>
								<td>15,879</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/05</td>
								<td>토</td>
								<td>롯데</td>
								<td>SSG</td>
								<td>사직</td>
								<td>10,670</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/05</td>
								<td>토</td>
								<td>NC</td>
								<td>키움</td>
								<td>창원</td>
								<td>8,244</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/06</td>
								<td>일</td>
								<td>KIA</td>
								<td>한화</td>
								<td>광주</td>
								<td>10,125</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/06</td>
								<td>일</td>
								<td>두산</td>
								<td>KT</td>
								<td>잠실</td>
								<td>6,744</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/06</td>
								<td>일</td>
								<td>삼성</td>
								<td>LG</td>
								<td>대구</td>
								<td>11,446</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/06</td>
								<td>일</td>
								<td>롯데</td>
								<td>SSG</td>
								<td>사직</td>
								<td>8,162</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/06</td>
								<td>일</td>
								<td>NC</td>
								<td>키움</td>
								<td>창원</td>
								<td>6,583</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/08</td>
								<td>화</td>
								<td>KT</td>
								<td>한화</td>
								<td>수원</td>
								<td>9,704</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/08</td>
								<td>화</td>
								<td>키움</td>
								<td>롯데</td>
								<td>고척</td>
								<td>8,376</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/08</td>
								<td>화</td>
								<td>SSG</td>
								<td>NC</td>
								<td>문학</td>
								<td>8,131</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/08</td>
								<td>화</td>
								<td>두산</td>
								<td>삼성</td>
								<td>잠실</td>
								<td>8,519</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/09</td>
								<td>수</td>
								<td>KT</td>
								<td>한화</td>
								<td>수원</td>
								<td>10,099</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/09</td>
								<td>수</td>
								<td>KIA</td>
								<td>LG</td>
								<td>광주</td>
								<td>3,700</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/09</td>
								<td>수</td>
								<td>키움</td>
								<td>롯데</td>
								<td>고척</td>
								<td>7,424</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/09</td>
								<td>수</td>
								<td>SSG</td>
								<td>NC</td>
								<td>문학</td>
								<td>6,473</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/09</td>
								<td>수</td>
								<td>두산</td>
								<td>삼성</td>
								<td>잠실</td>
								<td>8,344</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/10</td>
								<td>목</td>
								<td>키움</td>
								<td>롯데</td>
								<td>고척</td>
								<td>6,240</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/11</td>
								<td>금</td>
								<td>롯데</td>
								<td>KIA</td>
								<td>사직</td>
								<td>10,118</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/11</td>
								<td>금</td>
								<td>KT</td>
								<td>NC</td>
								<td>수원</td>
								<td>5,969</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/11</td>
								<td>금</td>
								<td>한화</td>
								<td>두산</td>
								<td>대전</td>
								<td>7,333</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/11</td>
								<td>금</td>
								<td>SSG</td>
								<td>삼성</td>
								<td>문학</td>
								<td>7,495</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/11</td>
								<td>금</td>
								<td>LG</td>
								<td>키움</td>
								<td>잠실</td>
								<td>11,910</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/12</td>
								<td>토</td>
								<td>롯데</td>
								<td>KIA</td>
								<td>사직</td>
								<td>16,677</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/12</td>
								<td>토</td>
								<td>KT</td>
								<td>NC</td>
								<td>수원</td>
								<td>10,138</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/12</td>
								<td>토</td>
								<td>한화</td>
								<td>두산</td>
								<td>대전</td>
								<td>12,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/12</td>
								<td>토</td>
								<td>SSG</td>
								<td>삼성</td>
								<td>문학</td>
								<td>18,055</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/12</td>
								<td>토</td>
								<td>LG</td>
								<td>키움</td>
								<td>잠실</td>
								<td>17,624</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/13</td>
								<td>일</td>
								<td>롯데</td>
								<td>KIA</td>
								<td>사직</td>
								<td>14,325</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/13</td>
								<td>일</td>
								<td>KT</td>
								<td>NC</td>
								<td>수원</td>
								<td>9,736</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/13</td>
								<td>일</td>
								<td>한화</td>
								<td>두산</td>
								<td>대전</td>
								<td>11,007</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/13</td>
								<td>일</td>
								<td>SSG</td>
								<td>삼성</td>
								<td>문학</td>
								<td>16,473</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/13</td>
								<td>일</td>
								<td>LG</td>
								<td>키움</td>
								<td>잠실</td>
								<td>18,279</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/15</td>
								<td>화</td>
								<td>NC</td>
								<td>한화</td>
								<td>창원</td>
								<td>10,116</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/15</td>
								<td>화</td>
								<td>두산</td>
								<td>KT</td>
								<td>잠실</td>
								<td>11,069</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/15</td>
								<td>화</td>
								<td>삼성</td>
								<td>LG</td>
								<td>대구</td>
								<td>14,248</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/15</td>
								<td>화</td>
								<td>롯데</td>
								<td>SSG</td>
								<td>사직</td>
								<td>11,871</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/15</td>
								<td>화</td>
								<td>KIA</td>
								<td>키움</td>
								<td>광주</td>
								<td>11,541</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/16</td>
								<td>수</td>
								<td>NC</td>
								<td>한화</td>
								<td>창원</td>
								<td>5,033</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/16</td>
								<td>수</td>
								<td>두산</td>
								<td>KT</td>
								<td>잠실</td>
								<td>5,160</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/16</td>
								<td>수</td>
								<td>삼성</td>
								<td>LG</td>
								<td>대구</td>
								<td>7,441</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/16</td>
								<td>수</td>
								<td>롯데</td>
								<td>SSG</td>
								<td>사직</td>
								<td>10,542</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/16</td>
								<td>수</td>
								<td>KIA</td>
								<td>키움</td>
								<td>광주</td>
								<td>7,050</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/17</td>
								<td>목</td>
								<td>NC</td>
								<td>한화</td>
								<td>창원</td>
								<td>4,875</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/17</td>
								<td>목</td>
								<td>두산</td>
								<td>KT</td>
								<td>잠실</td>
								<td>4,943</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/17</td>
								<td>목</td>
								<td>삼성</td>
								<td>LG</td>
								<td>대구</td>
								<td>7,415</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/17</td>
								<td>목</td>
								<td>롯데</td>
								<td>SSG</td>
								<td>사직</td>
								<td>9,843</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/17</td>
								<td>목</td>
								<td>KIA</td>
								<td>키움</td>
								<td>광주</td>
								<td>6,159</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/18</td>
								<td>금</td>
								<td>삼성</td>
								<td>KIA</td>
								<td>대구</td>
								<td>10,630</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/18</td>
								<td>금</td>
								<td>한화</td>
								<td>KT</td>
								<td>대전</td>
								<td>7,003</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/18</td>
								<td>금</td>
								<td>SSG</td>
								<td>LG</td>
								<td>문학</td>
								<td>14,549</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/18</td>
								<td>금</td>
								<td>키움</td>
								<td>롯데</td>
								<td>고척</td>
								<td>8,817</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/19</td>
								<td>토</td>
								<td>삼성</td>
								<td>KIA</td>
								<td>대구</td>
								<td>17,448</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/19</td>
								<td>토</td>
								<td>한화</td>
								<td>KT</td>
								<td>대전</td>
								<td>11,606</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/19</td>
								<td>토</td>
								<td>SSG</td>
								<td>LG</td>
								<td>문학</td>
								<td>23,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/19</td>
								<td>토</td>
								<td>키움</td>
								<td>롯데</td>
								<td>고척</td>
								<td>13,423</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/19</td>
								<td>토</td>
								<td>두산</td>
								<td>NC</td>
								<td>잠실</td>
								<td>12,240</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/20</td>
								<td>일</td>
								<td>삼성</td>
								<td>KIA</td>
								<td>대구</td>
								<td>12,586</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/20</td>
								<td>일</td>
								<td>한화</td>
								<td>KT</td>
								<td>대전</td>
								<td>8,762</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/20</td>
								<td>일</td>
								<td>SSG</td>
								<td>LG</td>
								<td>문학</td>
								<td>18,441</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/20</td>
								<td>일</td>
								<td>키움</td>
								<td>롯데</td>
								<td>고척</td>
								<td>12,545</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/20</td>
								<td>일</td>
								<td>두산</td>
								<td>NC</td>
								<td>잠실</td>
								<td>8,286</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/22</td>
								<td>화</td>
								<td>KT</td>
								<td>KIA</td>
								<td>수원</td>
								<td>7,916</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/22</td>
								<td>화</td>
								<td>키움</td>
								<td>두산</td>
								<td>고척</td>
								<td>6,455</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/22</td>
								<td>화</td>
								<td>한화</td>
								<td>삼성</td>
								<td>대전</td>
								<td>5,806</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/23</td>
								<td>수</td>
								<td>키움</td>
								<td>두산</td>
								<td>고척</td>
								<td>6,455</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/24</td>
								<td>목</td>
								<td>KT</td>
								<td>KIA</td>
								<td>수원</td>
								<td>9,846</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/24</td>
								<td>목</td>
								<td>LG</td>
								<td>롯데</td>
								<td>잠실</td>
								<td>15,547</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/24</td>
								<td>목</td>
								<td>SSG</td>
								<td>NC</td>
								<td>문학</td>
								<td>6,683</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/24</td>
								<td>목</td>
								<td>키움</td>
								<td>두산</td>
								<td>고척</td>
								<td>6,819</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/25</td>
								<td>금</td>
								<td>KIA</td>
								<td>한화</td>
								<td>광주</td>
								<td>8,457</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/25</td>
								<td>금</td>
								<td>롯데</td>
								<td>KT</td>
								<td>사직</td>
								<td>10,709</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/25</td>
								<td>금</td>
								<td>NC</td>
								<td>LG</td>
								<td>창원</td>
								<td>9,288</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/25</td>
								<td>금</td>
								<td>두산</td>
								<td>SSG</td>
								<td>잠실</td>
								<td>8,363</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/25</td>
								<td>금</td>
								<td>삼성</td>
								<td>키움</td>
								<td>대구</td>
								<td>11,135</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/26</td>
								<td>토</td>
								<td>KIA</td>
								<td>한화</td>
								<td>광주</td>
								<td>16,812</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/26</td>
								<td>토</td>
								<td>롯데</td>
								<td>KT</td>
								<td>사직</td>
								<td>15,657</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/26</td>
								<td>토</td>
								<td>NC</td>
								<td>LG</td>
								<td>창원</td>
								<td>13,484</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/26</td>
								<td>토</td>
								<td>두산</td>
								<td>SSG</td>
								<td>잠실</td>
								<td>15,101</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/26</td>
								<td>토</td>
								<td>삼성</td>
								<td>키움</td>
								<td>대구</td>
								<td>17,586</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/27</td>
								<td>일</td>
								<td>KIA</td>
								<td>한화</td>
								<td>광주</td>
								<td>12,627</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/27</td>
								<td>일</td>
								<td>롯데</td>
								<td>KT</td>
								<td>사직</td>
								<td>10,735</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/27</td>
								<td>일</td>
								<td>NC</td>
								<td>LG</td>
								<td>창원</td>
								<td>8,771</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/27</td>
								<td>일</td>
								<td>두산</td>
								<td>SSG</td>
								<td>잠실</td>
								<td>11,300</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/27</td>
								<td>일</td>
								<td>삼성</td>
								<td>키움</td>
								<td>대구</td>
								<td>13,461</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/30</td>
								<td>수</td>
								<td>SSG</td>
								<td>키움</td>
								<td>문학</td>
								<td>7,809</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/31</td>
								<td>목</td>
								<td>한화</td>
								<td>롯데</td>
								<td>대전</td>
								<td>7,179</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/31</td>
								<td>목</td>
								<td>KIA</td>
								<td>NC</td>
								<td>광주</td>
								<td>7,152</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/31</td>
								<td>목</td>
								<td>LG</td>
								<td>두산</td>
								<td>잠실</td>
								<td>17,859</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/31</td>
								<td>목</td>
								<td>KT</td>
								<td>삼성</td>
								<td>수원</td>
								<td>8,071</td>
							</tr>
						
							<tr class="order">
								<td>2023/08/31</td>
								<td>목</td>
								<td>SSG</td>
								<td>키움</td>
								<td>문학</td>
								<td>9,780</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/01</td>
								<td>금</td>
								<td>LG</td>
								<td>한화</td>
								<td>잠실</td>
								<td>20,381</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/01</td>
								<td>금</td>
								<td>SSG</td>
								<td>KIA</td>
								<td>문학</td>
								<td>17,281</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/01</td>
								<td>금</td>
								<td>키움</td>
								<td>KT</td>
								<td>고척</td>
								<td>3,746</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/01</td>
								<td>금</td>
								<td>삼성</td>
								<td>NC</td>
								<td>대구</td>
								<td>12,843</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/02</td>
								<td>토</td>
								<td>LG</td>
								<td>한화</td>
								<td>잠실</td>
								<td>23,574</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/02</td>
								<td>토</td>
								<td>SSG</td>
								<td>KIA</td>
								<td>문학</td>
								<td>23,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/02</td>
								<td>토</td>
								<td>키움</td>
								<td>KT</td>
								<td>고척</td>
								<td>6,731</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/02</td>
								<td>토</td>
								<td>삼성</td>
								<td>NC</td>
								<td>대구</td>
								<td>20,468</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/03</td>
								<td>일</td>
								<td>LG</td>
								<td>한화</td>
								<td>잠실</td>
								<td>22,858</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/03</td>
								<td>일</td>
								<td>SSG</td>
								<td>KIA</td>
								<td>문학</td>
								<td>23,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/03</td>
								<td>일</td>
								<td>키움</td>
								<td>KT</td>
								<td>고척</td>
								<td>5,778</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/03</td>
								<td>일</td>
								<td>삼성</td>
								<td>NC</td>
								<td>대구</td>
								<td>14,601</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/03</td>
								<td>일</td>
								<td>롯데</td>
								<td>두산</td>
								<td>사직</td>
								<td>11,436</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/04</td>
								<td>월</td>
								<td>롯데</td>
								<td>두산</td>
								<td>사직</td>
								<td>4,621</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/05</td>
								<td>화</td>
								<td>KT</td>
								<td>LG</td>
								<td>수원</td>
								<td>10,153</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/05</td>
								<td>화</td>
								<td>한화</td>
								<td>SSG</td>
								<td>대전</td>
								<td>5,124</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/05</td>
								<td>화</td>
								<td>롯데</td>
								<td>삼성</td>
								<td>울산</td>
								<td>5,999</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/05</td>
								<td>화</td>
								<td>NC</td>
								<td>키움</td>
								<td>창원</td>
								<td>3,511</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/06</td>
								<td>수</td>
								<td>두산</td>
								<td>KIA</td>
								<td>잠실</td>
								<td>20,468</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/06</td>
								<td>수</td>
								<td>KT</td>
								<td>LG</td>
								<td>수원</td>
								<td>10,075</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/06</td>
								<td>수</td>
								<td>한화</td>
								<td>SSG</td>
								<td>대전</td>
								<td>7,213</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/06</td>
								<td>수</td>
								<td>롯데</td>
								<td>삼성</td>
								<td>울산</td>
								<td>6,380</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/06</td>
								<td>수</td>
								<td>NC</td>
								<td>키움</td>
								<td>창원</td>
								<td>4,269</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/07</td>
								<td>목</td>
								<td>두산</td>
								<td>KIA</td>
								<td>잠실</td>
								<td>21,838</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/07</td>
								<td>목</td>
								<td>KT</td>
								<td>LG</td>
								<td>수원</td>
								<td>10,799</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/07</td>
								<td>목</td>
								<td>한화</td>
								<td>SSG</td>
								<td>대전</td>
								<td>7,236</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/07</td>
								<td>목</td>
								<td>롯데</td>
								<td>삼성</td>
								<td>울산</td>
								<td>7,156</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/07</td>
								<td>목</td>
								<td>NC</td>
								<td>키움</td>
								<td>창원</td>
								<td>4,780</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/08</td>
								<td>금</td>
								<td>키움</td>
								<td>한화</td>
								<td>고척</td>
								<td>7,715</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/08</td>
								<td>금</td>
								<td>KIA</td>
								<td>LG</td>
								<td>광주</td>
								<td>12,280</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/08</td>
								<td>금</td>
								<td>NC</td>
								<td>롯데</td>
								<td>창원</td>
								<td>12,684</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/08</td>
								<td>금</td>
								<td>KT</td>
								<td>SSG</td>
								<td>수원</td>
								<td>7,200</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/08</td>
								<td>금</td>
								<td>두산</td>
								<td>삼성</td>
								<td>잠실</td>
								<td>15,991</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/09</td>
								<td>토</td>
								<td>키움</td>
								<td>한화</td>
								<td>고척</td>
								<td>9,962</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/09</td>
								<td>토</td>
								<td>키움</td>
								<td>한화</td>
								<td>고척</td>
								<td>10,028</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/09</td>
								<td>토</td>
								<td>KIA</td>
								<td>LG</td>
								<td>광주</td>
								<td>11,820</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/09</td>
								<td>토</td>
								<td>KIA</td>
								<td>LG</td>
								<td>광주</td>
								<td>18,462</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/09</td>
								<td>토</td>
								<td>NC</td>
								<td>롯데</td>
								<td>창원</td>
								<td>10,933</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/09</td>
								<td>토</td>
								<td>NC</td>
								<td>롯데</td>
								<td>창원</td>
								<td>17,861</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/09</td>
								<td>토</td>
								<td>KT</td>
								<td>SSG</td>
								<td>수원</td>
								<td>13,739</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/09</td>
								<td>토</td>
								<td>두산</td>
								<td>삼성</td>
								<td>잠실</td>
								<td>14,279</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/09</td>
								<td>토</td>
								<td>두산</td>
								<td>삼성</td>
								<td>잠실</td>
								<td>21,514</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/10</td>
								<td>일</td>
								<td>키움</td>
								<td>한화</td>
								<td>고척</td>
								<td>11,313</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/10</td>
								<td>일</td>
								<td>KIA</td>
								<td>LG</td>
								<td>광주</td>
								<td>13,948</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/10</td>
								<td>일</td>
								<td>NC</td>
								<td>롯데</td>
								<td>창원</td>
								<td>13,984</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/10</td>
								<td>일</td>
								<td>KT</td>
								<td>SSG</td>
								<td>수원</td>
								<td>11,212</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/10</td>
								<td>일</td>
								<td>두산</td>
								<td>삼성</td>
								<td>잠실</td>
								<td>17,467</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/12</td>
								<td>화</td>
								<td>두산</td>
								<td>한화</td>
								<td>잠실</td>
								<td>10,169</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/12</td>
								<td>화</td>
								<td>삼성</td>
								<td>KIA</td>
								<td>대구</td>
								<td>9,037</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/12</td>
								<td>화</td>
								<td>SSG</td>
								<td>KT</td>
								<td>문학</td>
								<td>10,309</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/12</td>
								<td>화</td>
								<td>롯데</td>
								<td>NC</td>
								<td>사직</td>
								<td>8,202</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/13</td>
								<td>수</td>
								<td>NC</td>
								<td>KT</td>
								<td>창원</td>
								<td>3,919</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/13</td>
								<td>수</td>
								<td>KIA</td>
								<td>롯데</td>
								<td>광주</td>
								<td>6,323</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/14</td>
								<td>목</td>
								<td>삼성</td>
								<td>KT</td>
								<td>대구</td>
								<td>6,850</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/14</td>
								<td>목</td>
								<td>두산</td>
								<td>SSG</td>
								<td>잠실</td>
								<td>7,257</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/15</td>
								<td>금</td>
								<td>한화</td>
								<td>LG</td>
								<td>대전</td>
								<td>5,724</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/15</td>
								<td>금</td>
								<td>KIA</td>
								<td>두산</td>
								<td>광주</td>
								<td>7,350</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/15</td>
								<td>금</td>
								<td>NC</td>
								<td>삼성</td>
								<td>창원</td>
								<td>4,129</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/15</td>
								<td>금</td>
								<td>롯데</td>
								<td>키움</td>
								<td>사직</td>
								<td>6,409</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/16</td>
								<td>토</td>
								<td>LG</td>
								<td>SSG</td>
								<td>잠실</td>
								<td>18,576</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/17</td>
								<td>일</td>
								<td>한화</td>
								<td>KT</td>
								<td>대전</td>
								<td>7,406</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/17</td>
								<td>일</td>
								<td>한화</td>
								<td>KT</td>
								<td>대전</td>
								<td>6,228</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/17</td>
								<td>일</td>
								<td>삼성</td>
								<td>롯데</td>
								<td>대구</td>
								<td>18,746</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/17</td>
								<td>일</td>
								<td>KIA</td>
								<td>두산</td>
								<td>광주</td>
								<td>12,878</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/17</td>
								<td>일</td>
								<td>LG</td>
								<td>SSG</td>
								<td>잠실</td>
								<td>15,193</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/17</td>
								<td>일</td>
								<td>LG</td>
								<td>SSG</td>
								<td>잠실</td>
								<td>14,237</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/18</td>
								<td>월</td>
								<td>한화</td>
								<td>KT</td>
								<td>대전</td>
								<td>3,425</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/18</td>
								<td>월</td>
								<td>KIA</td>
								<td>두산</td>
								<td>광주</td>
								<td>3,482</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/19</td>
								<td>화</td>
								<td>KIA</td>
								<td>LG</td>
								<td>광주</td>
								<td>8,871</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/19</td>
								<td>화</td>
								<td>두산</td>
								<td>NC</td>
								<td>잠실</td>
								<td>6,726</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/19</td>
								<td>화</td>
								<td>한화</td>
								<td>SSG</td>
								<td>대전</td>
								<td>4,014</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/19</td>
								<td>화</td>
								<td>KT</td>
								<td>삼성</td>
								<td>수원</td>
								<td>7,216</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/19</td>
								<td>화</td>
								<td>롯데</td>
								<td>키움</td>
								<td>사직</td>
								<td>5,523</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/21</td>
								<td>목</td>
								<td>한화</td>
								<td>KIA</td>
								<td>대전</td>
								<td>7,747</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/21</td>
								<td>목</td>
								<td>SSG</td>
								<td>LG</td>
								<td>문학</td>
								<td>12,353</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/21</td>
								<td>목</td>
								<td>KT</td>
								<td>롯데</td>
								<td>수원</td>
								<td>7,691</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/21</td>
								<td>목</td>
								<td>키움</td>
								<td>NC</td>
								<td>고척</td>
								<td>5,178</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/21</td>
								<td>목</td>
								<td>삼성</td>
								<td>두산</td>
								<td>대구</td>
								<td>7,596</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/22</td>
								<td>금</td>
								<td>KIA</td>
								<td>KT</td>
								<td>광주</td>
								<td>10,221</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/22</td>
								<td>금</td>
								<td>SSG</td>
								<td>롯데</td>
								<td>문학</td>
								<td>11,561</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/22</td>
								<td>금</td>
								<td>LG</td>
								<td>NC</td>
								<td>잠실</td>
								<td>16,269</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/22</td>
								<td>금</td>
								<td>삼성</td>
								<td>두산</td>
								<td>대구</td>
								<td>11,568</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/22</td>
								<td>금</td>
								<td>한화</td>
								<td>키움</td>
								<td>대전</td>
								<td>7,088</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/23</td>
								<td>토</td>
								<td>LG</td>
								<td>한화</td>
								<td>잠실</td>
								<td>22,765</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/23</td>
								<td>토</td>
								<td>KIA</td>
								<td>KT</td>
								<td>광주</td>
								<td>13,846</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/23</td>
								<td>토</td>
								<td>SSG</td>
								<td>롯데</td>
								<td>문학</td>
								<td>19,725</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/23</td>
								<td>토</td>
								<td>NC</td>
								<td>두산</td>
								<td>창원</td>
								<td>11,026</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/24</td>
								<td>일</td>
								<td>LG</td>
								<td>한화</td>
								<td>잠실</td>
								<td>20,369</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/24</td>
								<td>일</td>
								<td>KIA</td>
								<td>KT</td>
								<td>광주</td>
								<td>10,108</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/24</td>
								<td>일</td>
								<td>SSG</td>
								<td>롯데</td>
								<td>문학</td>
								<td>16,280</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/24</td>
								<td>일</td>
								<td>NC</td>
								<td>두산</td>
								<td>창원</td>
								<td>8,247</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/26</td>
								<td>화</td>
								<td>NC</td>
								<td>KIA</td>
								<td>창원</td>
								<td>6,945</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/27</td>
								<td>수</td>
								<td>NC</td>
								<td>KIA</td>
								<td>창원</td>
								<td>3,775</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/27</td>
								<td>수</td>
								<td>NC</td>
								<td>KIA</td>
								<td>창원</td>
								<td>8,190</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/27</td>
								<td>수</td>
								<td>LG</td>
								<td>KT</td>
								<td>잠실</td>
								<td>5,656</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/27</td>
								<td>수</td>
								<td>LG</td>
								<td>KT</td>
								<td>잠실</td>
								<td>14,733</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/27</td>
								<td>수</td>
								<td>SSG</td>
								<td>두산</td>
								<td>문학</td>
								<td>6,526</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/27</td>
								<td>수</td>
								<td>SSG</td>
								<td>두산</td>
								<td>문학</td>
								<td>12,132</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/27</td>
								<td>수</td>
								<td>한화</td>
								<td>삼성</td>
								<td>대전</td>
								<td>2,807</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/27</td>
								<td>수</td>
								<td>한화</td>
								<td>삼성</td>
								<td>대전</td>
								<td>7,281</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/28</td>
								<td>목</td>
								<td>롯데</td>
								<td>한화</td>
								<td>사직</td>
								<td>12,227</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/28</td>
								<td>목</td>
								<td>NC</td>
								<td>KIA</td>
								<td>창원</td>
								<td>11,864</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/28</td>
								<td>목</td>
								<td>키움</td>
								<td>SSG</td>
								<td>고척</td>
								<td>7,082</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/28</td>
								<td>목</td>
								<td>LG</td>
								<td>삼성</td>
								<td>잠실</td>
								<td>21,057</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/29</td>
								<td>금</td>
								<td>롯데</td>
								<td>한화</td>
								<td>사직</td>
								<td>10,279</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/29</td>
								<td>금</td>
								<td>키움</td>
								<td>KIA</td>
								<td>고척</td>
								<td>14,472</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/29</td>
								<td>금</td>
								<td>두산</td>
								<td>LG</td>
								<td>잠실</td>
								<td>20,951</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/30</td>
								<td>토</td>
								<td>SSG</td>
								<td>KIA</td>
								<td>문학</td>
								<td>22,191</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/30</td>
								<td>토</td>
								<td>두산</td>
								<td>LG</td>
								<td>잠실</td>
								<td>23,750</td>
							</tr>
						
							<tr class="order">
								<td>2023/09/30</td>
								<td>토</td>
								<td>삼성</td>
								<td>NC</td>
								<td>대구</td>
								<td>24,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/01</td>
								<td>일</td>
								<td>SSG</td>
								<td>KIA</td>
								<td>문학</td>
								<td>22,701</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/01</td>
								<td>일</td>
								<td>두산</td>
								<td>LG</td>
								<td>잠실</td>
								<td>23,750</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/01</td>
								<td>일</td>
								<td>한화</td>
								<td>NC</td>
								<td>대전</td>
								<td>11,004</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/01</td>
								<td>일</td>
								<td>롯데</td>
								<td>삼성</td>
								<td>사직</td>
								<td>20,159</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/01</td>
								<td>일</td>
								<td>KT</td>
								<td>키움</td>
								<td>수원</td>
								<td>11,337</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/02</td>
								<td>월</td>
								<td>KT</td>
								<td>LG</td>
								<td>수원</td>
								<td>18,700</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/02</td>
								<td>월</td>
								<td>한화</td>
								<td>NC</td>
								<td>대전</td>
								<td>12,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/02</td>
								<td>월</td>
								<td>롯데</td>
								<td>삼성</td>
								<td>사직</td>
								<td>15,868</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/02</td>
								<td>월</td>
								<td>롯데</td>
								<td>삼성</td>
								<td>사직</td>
								<td>16,293</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/02</td>
								<td>월</td>
								<td>두산</td>
								<td>키움</td>
								<td>잠실</td>
								<td>18,050</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/03</td>
								<td>화</td>
								<td>KT</td>
								<td>KIA</td>
								<td>수원</td>
								<td>16,841</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/03</td>
								<td>화</td>
								<td>SSG</td>
								<td>NC</td>
								<td>문학</td>
								<td>14,507</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/03</td>
								<td>화</td>
								<td>롯데</td>
								<td>삼성</td>
								<td>사직</td>
								<td>13,042</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/03</td>
								<td>화</td>
								<td>두산</td>
								<td>키움</td>
								<td>잠실</td>
								<td>14,588</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/04</td>
								<td>수</td>
								<td>삼성</td>
								<td>한화</td>
								<td>대구</td>
								<td>12,571</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/04</td>
								<td>수</td>
								<td>KT</td>
								<td>KIA</td>
								<td>수원</td>
								<td>3,908</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/04</td>
								<td>수</td>
								<td>KT</td>
								<td>KIA</td>
								<td>수원</td>
								<td>5,907</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/04</td>
								<td>수</td>
								<td>롯데</td>
								<td>LG</td>
								<td>사직</td>
								<td>6,970</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/04</td>
								<td>수</td>
								<td>SSG</td>
								<td>NC</td>
								<td>문학</td>
								<td>8,006</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/05</td>
								<td>목</td>
								<td>삼성</td>
								<td>한화</td>
								<td>대구</td>
								<td>14,483</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/05</td>
								<td>목</td>
								<td>KT</td>
								<td>KIA</td>
								<td>수원</td>
								<td>7,264</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/05</td>
								<td>목</td>
								<td>롯데</td>
								<td>LG</td>
								<td>사직</td>
								<td>10,040</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/05</td>
								<td>목</td>
								<td>SSG</td>
								<td>NC</td>
								<td>문학</td>
								<td>9,004</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/06</td>
								<td>금</td>
								<td>SSG</td>
								<td>한화</td>
								<td>문학</td>
								<td>15,755</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/06</td>
								<td>금</td>
								<td>LG</td>
								<td>KIA</td>
								<td>잠실</td>
								<td>23,750</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/06</td>
								<td>금</td>
								<td>KT</td>
								<td>삼성</td>
								<td>수원</td>
								<td>8,132</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/07</td>
								<td>토</td>
								<td>KT</td>
								<td>한화</td>
								<td>수원</td>
								<td>15,210</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/07</td>
								<td>토</td>
								<td>키움</td>
								<td>LG</td>
								<td>고척</td>
								<td>13,301</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/07</td>
								<td>토</td>
								<td>두산</td>
								<td>롯데</td>
								<td>잠실</td>
								<td>19,916</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/07</td>
								<td>토</td>
								<td>NC</td>
								<td>SSG</td>
								<td>창원</td>
								<td>13,479</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/08</td>
								<td>일</td>
								<td>KT</td>
								<td>한화</td>
								<td>수원</td>
								<td>15,197</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/08</td>
								<td>일</td>
								<td>두산</td>
								<td>롯데</td>
								<td>잠실</td>
								<td>21,392</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/08</td>
								<td>일</td>
								<td>NC</td>
								<td>SSG</td>
								<td>창원</td>
								<td>10,073</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/08</td>
								<td>일</td>
								<td>KIA</td>
								<td>삼성</td>
								<td>광주</td>
								<td>16,005</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/09</td>
								<td>월</td>
								<td>NC</td>
								<td>한화</td>
								<td>창원</td>
								<td>8,716</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/09</td>
								<td>월</td>
								<td>LG</td>
								<td>롯데</td>
								<td>잠실</td>
								<td>22,807</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/09</td>
								<td>월</td>
								<td>KIA</td>
								<td>삼성</td>
								<td>광주</td>
								<td>12,758</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/10</td>
								<td>화</td>
								<td>NC</td>
								<td>한화</td>
								<td>창원</td>
								<td>7,342</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/10</td>
								<td>화</td>
								<td>LG</td>
								<td>롯데</td>
								<td>잠실</td>
								<td>18,521</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/10</td>
								<td>화</td>
								<td>KT</td>
								<td>두산</td>
								<td>수원</td>
								<td>10,937</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/10</td>
								<td>화</td>
								<td>KIA</td>
								<td>SSG</td>
								<td>광주</td>
								<td>8,333</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/10</td>
								<td>화</td>
								<td>키움</td>
								<td>삼성</td>
								<td>고척</td>
								<td>11,757</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/11</td>
								<td>수</td>
								<td>롯데</td>
								<td>두산</td>
								<td>사직</td>
								<td>9,940</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/11</td>
								<td>수</td>
								<td>KIA</td>
								<td>키움</td>
								<td>광주</td>
								<td>3,656</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/12</td>
								<td>목</td>
								<td>KIA</td>
								<td>롯데</td>
								<td>광주</td>
								<td>4,767</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/12</td>
								<td>목</td>
								<td>두산</td>
								<td>NC</td>
								<td>잠실</td>
								<td>7,113</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/13</td>
								<td>금</td>
								<td>두산</td>
								<td>KIA</td>
								<td>잠실</td>
								<td>19,188</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/13</td>
								<td>금</td>
								<td>NC</td>
								<td>LG</td>
								<td>창원</td>
								<td>6,257</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/13</td>
								<td>금</td>
								<td>SSG</td>
								<td>키움</td>
								<td>문학</td>
								<td>16,783</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/14</td>
								<td>토</td>
								<td>한화</td>
								<td>롯데</td>
								<td>대전</td>
								<td>9,153</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/14</td>
								<td>토</td>
								<td>LG</td>
								<td>두산</td>
								<td>잠실</td>
								<td>21,771</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/14</td>
								<td>토</td>
								<td>삼성</td>
								<td>SSG</td>
								<td>대구</td>
								<td>24,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/15</td>
								<td>일</td>
								<td>한화</td>
								<td>롯데</td>
								<td>대전</td>
								<td>9,840</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/15</td>
								<td>일</td>
								<td>LG</td>
								<td>두산</td>
								<td>잠실</td>
								<td>23,750</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/15</td>
								<td>일</td>
								<td>NC</td>
								<td>삼성</td>
								<td>창원</td>
								<td>17,861</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/16</td>
								<td>월</td>
								<td>한화</td>
								<td>롯데</td>
								<td>대전</td>
								<td>12,000</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/16</td>
								<td>월</td>
								<td>KIA</td>
								<td>NC</td>
								<td>광주</td>
								<td>5,251</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/16</td>
								<td>월</td>
								<td>두산</td>
								<td>SSG</td>
								<td>잠실</td>
								<td>15,850</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/17</td>
								<td>화</td>
								<td>KIA</td>
								<td>NC</td>
								<td>광주</td>
								<td>10,175</td>
							</tr>
						
							<tr class="order">
								<td>2023/10/17</td>
								<td>화</td>
								<td>SSG</td>
								<td>두산</td>
								<td>문학</td>
								<td>21,007</td>
							</tr>
						
					</tbody>
				</table>
"""
